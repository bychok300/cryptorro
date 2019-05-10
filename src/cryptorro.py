import argparse

import sys

parser = argparse.ArgumentParser(description='Encryption tool for encrypting whole files in folders')

parser.add_argument("-p", dest="path", type=str, help="Path to folder.")
parser.add_argument("-e", dest="encrypt", action="store_true", help="Encrypt every file in folder")
parser.add_argument("-d", dest="decrypt", action="store_true", help="Decrypt every file in folder")

options = parser.parse_args()

if len(sys.argv) < 4:
    parser.print_help()
    sys.exit(1)

# stupid hack that allow call getPass only when num of args is valid
from AESCipher import AESCipher
from FileUtils import FileUtils

files = FileUtils.recursiv_list_files_in(options.path)
for file in files:
    if options.encrypt:
        try:
            FileUtils.replace_file_content(file, AESCipher().encrypt(FileUtils.read_file(file)))
        except:
            print("Error in " + file + " possibly can not encrypt file")
    else:
        try:
            FileUtils.replace_file_content(file, AESCipher().decrypt(FileUtils.read_file(file)))
        except:
            print("Error in " + file + " possibly can not decrypt file")
