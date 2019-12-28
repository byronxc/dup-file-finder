#!/usr/bin/python

import sys
import os
import hashlib  
from pathlib import Path

def hashfile(path, blocksize = 65536):
    streamFile = open(path, 'rb')
    hasher = hashlib.md5()
    buffer = streamFile.read(blocksize)
    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = streamFile.read(blocksize)
    streamFile.close()
    return hasher.hexdigest()

def findDuplicateDictValues(dictionary):
    for key, value in dictionary.items():
        for key2, value2 in dictionary.items():
            if key != key2 and value == value2:
                print("\nDuplicate files:")
                print("File 1: " + key) 
                print("File 2: " + key2 + "\n")
                print("1: Delete first file")
                print("2: Delete second file")
                print("3: Cancel\n")
                option = input()
                if(option == '1'):
                     os.remove(key)
                elif(option == '2'):
                     os.remove(key2)
                else:
                    continue

folder = "./"
if(len(sys.argv) > 1):
    folder = sys.argv[1]

paths = list(Path(folder).rglob("*.*"))
hashes = {}

for path in paths:
    if os.path.isfile(path):
       fileText = hashfile(path)
       hashes[str(path)] = str(fileText)

findDuplicateDictValues(hashes)