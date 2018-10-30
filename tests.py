from firewall import *

class TestClass(object):
    # basic test case
    def test_one(self):
        firewall = Firewall("./test.csv")
        assert firewall.accept_packet("inbound", "tcp", 80, "192.168.1.2") == True

    # failing test case
    def test_two(self):
        firewall = Firewall("./test.csv")
        assert firewall.accept_packet("inbound", "udp", 53, "192.168.1.2") == False
    
    # read default csv test case
    def test_three(self):
        firewall = Firewall()
        assert firewall.accept_packet("inbound", "udp", 53, "192.168.1.2") == False
    
    # no direction type available test case
    def test_four(self):
        firewall = Firewall("./test.csv")
        assert firewall.accept_packet("outbounds", "udp", 53, "192.168.1.2") == False

    # no port range available test case
    def test_five(self):
        firewall = Firewall("./test.csv")
        assert firewall.accept_packet("inbound", "udp", 244343553, "192.168.1.2") == False

    # no ip available in range test case
    def test_six(self):
        firewall = Firewall("./test.csv")
        assert firewall.accept_packet("outbound", "udp", 53, "266.168.1.2") == False