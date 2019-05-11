import argparse
import sys

parser = argparse.ArgumentParser(description='Encryption tool for encrypting whole files in folders')

parser.add_argument("-p", dest="path", type=str, help="Path to folder.")
parser.add_argument("-f", dest="file", type=str, help="Path to file.")
parser.add_argument("-e", dest="encrypt", action="store_true", help="Encrypt every file in folder")
parser.add_argument("-d", dest="decrypt", action="store_true", help="Decrypt every file in folder")

options = parser.parse_args()

if len(sys.argv) < 4:
    parser.print_help()
    sys.exit(1)

# stupid hack to avoid call getPass only when num of args is valid
from AESCipher import AESCipher

if options.file is not None:
    AESCipher.encrypt_file(options)
else:
    AESCipher.encrypt_files_recurcive(options)
