# README

## 1. Overview

    * The project consists of a python file and one test file:
        * firewall.py
        * tests.py
    * The firewall.py file consists of the firewall class structure.
    * Overall the project is pretty self explanatory, I have also added comments for better understanidng.

## 2.Why Python and DataFrames

    * I wanted to make the program as efficient as possible, considering the fact that I used data frames to parse the rules csv file.
    * I was able to shorted and speed up my search drastically since I was able to use hashing to my advantage. Using data frames allowed me to maintain optimum space and time complexity.
  
## 3. How could I improve?

    * I think the last condition to check whether an ip_address was valid or not could be done using hashing, however, pandas did not allow me to compare two lists and hence I had to use a for loop and check the validity iteratively.
    * However, if I had enough time I believe I could have made the process more time efficient.
  
## 3.Compile and Run FireWall

    1. Extract the Firewall.zip file in your preferred location.

    2. Open command line in the extracted direcotry and install the requirements with
    ```
    pip install -r requirements.txt
    ```

    3. Run the tests with:
    ```
    pytest -q tests.py
    ```

## 4. Team
    
    I wish to work in the Platform team, I believe it is a good fit for my skillset and interests.
