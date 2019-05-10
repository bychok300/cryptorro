---
__Cryptorro - it is python console tool for encryption file in folders__

![Cryptorro](assets/cryptorro.png "Cryptorro")

    usage: cryptorro.py [-h] [-p PATH] [-e] [-d]

    Encryption tool for encrypting whole files in folders

    optional arguments:
      -h, --help  show this help message and exit
      -p PATH     Path to folder.
      -e          Encrypt every file in folder
      -d          Decrypt every file in folder


#### **installing**

    pip install -r requirements.txt


#### **example**
 

suppose we folder with text files:

    rootFolder
     |-example1.txt 
     |-example2.txt
     |-example3.txt

each file contain simple strings 
- Hello 
- Mister
- Hacker

after 

    python3 cryptorro.py -p ~/path_to_rootFolder -e
and passing encryption key strings in files will encrypted with **aes-256** and will look like that 
    
    sqJnynuGSI3ske7EtBcQ2my1mtvae+C1QiYd8nmgD6XGsqZzZ0AIdXm3wm+
