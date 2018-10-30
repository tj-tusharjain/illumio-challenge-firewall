import pandas as pd

class Firewall:
    def __init__(self, file_path="./file.csv"):
        self.firewall_df = pd.read_csv(file_path, names = ["direction", "protocol", "port", "ip_address"])
        self.parse_port_range()
        self.parse_IP_range()


    # accept packets function to accept a request if it is valid within the given rules
    def accept_packet(self, direction, protocol, port, ip_address):
        # eliminating non-matching directions
        sub_df = self.firewall_df.loc[self.firewall_df['direction'] == direction]
        if sub_df.empty:
            return False

        # eliminating non-matching protocols
        sub_df = sub_df.loc[sub_df['protocol'] == protocol]
        if sub_df.empty:
            return False

        # eliminating ports that are not in required range
        sub_df = sub_df.loc[(sub_df['start_port'] <= port) & (port <= sub_df['end_port'])]
        if sub_df.empty:
            return False

        # checking if the ip address is within range from the remaining rules
        ip_address_list = list(map(int, ip_address.split('.')))

        return self.check_ip(ip_address_list, sub_df)


    # a method to parse the port ranges in the given rules
    def parse_port_range(self):
        port_list = list(self.firewall_df['port'])
        start_ports = []
        end_ports = []

        for port in port_list:
            if "-" in port:
                numbers_for_range = port.split("-")
                start_ports.append(int(numbers_for_range[0]))
                end_ports.append(int(numbers_for_range[1]))
            else:
                start_ports.append(int(port))
                end_ports.append(int(port))
        
        self.firewall_df["start_port"] = pd.Series(start_ports)
        self.firewall_df["end_port"] = pd.Series(end_ports)


    # a method to parse the ip ranges in the given rules
    def parse_IP_range(self):
        ip_list = list(self.firewall_df['ip_address'])
        start_ips = []
        end_ips = []
        
        for ip in ip_list:
            if "-" in ip:
                ip_for_range = ip.split("-")
                lower_ip = list(map(int, ip_for_range[0].split('.')))
                upper_ip = list(map(int, ip_for_range[1].split('.')))
                
                start_ips.append(lower_ip)
                end_ips.append(upper_ip)
            else:
                start_ips.append(list(map(int, ip.split('.'))))
                end_ips.append(list(map(int, ip.split('.'))))
        
        self.firewall_df["start_ip"] = start_ips
        self.firewall_df["end_ip"] = end_ips
        

    # a method to check if the given ip address is present within the rules
    def check_ip(self, ip_address, sub_df):
        for index, row in sub_df.iterrows():
            current_start_ip = row['start_ip']
            current_end_ip = row['end_ip']
            if current_start_ip <= ip_address and ip_address <= current_end_ip:
                return True
        
        return False