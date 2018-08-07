#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:00:38 2018

@author: crantu
"""


import hashlib
import sys


def return_hash_from_iso(iso_filename):
    with open(iso_filename, 'rb') as f:
        checksum = hashlib.sha256(f.read()).hexdigest()

    return checksum


def check_hash_key(iso_filename):
    sha256_filename = iso_filename.replace(".iso", ".sha256")

    with open(sha256_filename, "r") as f:
        hash_value = return_hash_from_iso(iso_filename)
        sha256_file = f.readline().strip()
        if sha256_file == hash_value:
            print("OK")
        else:
            print("Error")


if __name__ == "__main__":
    check_hash_key(sys.argv[1])
