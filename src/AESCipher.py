import base64
import hashlib
from getpass import getpass
from Crypto import Random
from Crypto.Cipher import AES

from FileUtils import FileUtils


class AESCipher(object):
    key = getpass(prompt='Encryption key: ')

    def __init__(self):
        self.bs = 32
        self.key = hashlib.sha256(AESCipher.key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]

    @staticmethod
    def encrypt_files_recurcive(options):
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

    @staticmethod
    def encrypt_file(options):
        try:
            FileUtils.replace_file_content(options.file, AESCipher().encrypt(FileUtils.read_file(options.file)))
        except:
            print("Error in " + options.file + " possibly can not decrypt file")
