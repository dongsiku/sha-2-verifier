#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:00:38 2018

@author: crantu
"""


import hashlib
import sys
from os import path


class VerifySHA:
    def __init__(self, mainfilename):
        self.mainfilename = mainfilename

    def return_hash_from_mainfile(self, sha_num):
        with open(self.mainfilename, 'rb') as f:
            if sha_num == 256:
                checksum = hashlib.sha256(f.read()).hexdigest()
            elif sha_num == 512:
                checksum = hashlib.sha512(f.read()).hexdigest()
            print("Hash value: {}".format(checksum))

        return checksum


    def check_hash_key(self):
        sha256_filename = "{}.sha256".format(self.mainfilename.rsplit(".", 1)[0])
        sha512_filename = "{}.sha512".format(self.mainfilename.rsplit(".", 1)[0])
        if path.isfile(sha256_filename):
            sha_filename = sha256_filename
            sha_num = 256
        elif path.isfile(sha512_filename):
            sha_filename = sha512_filename
            sha_num = 512
        else:
            raise FileNotFoundError("No file *.sha256 or *.sh512")

        with open(sha_filename, "r") as f:
            hash_value = self.return_hash_from_mainfile(sha_num)
            sha_file = f.readline().strip()
            print(".sha{}: {}".format(sha_num, sha_file))
            if sha_file == hash_value:
                print("OK")
            else:
                print("Error")


if __name__ == "__main__":
    vsha = VerifySHA(sys.argv[1])
    vsha.check_hash_key()
