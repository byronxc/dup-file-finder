#!/usr/bin/python

import sys
import os
import hashlib
from pathlib import Path

def findDuplicateDictValues(dictionary):
    for key, value in dictionary.items():
        for key2, value2 in dictionary.items():
            print(value + ", " + value2)
            print(key + ", " + key2)
            print(key != key2)
            print(value == value2)
            
            if key != key2 and value == value2:
                print(key + ", " + key2)



folder = "./"

if(len(sys.argv) > 1):
    folder = sys.argv[1]

paths = list(Path(folder).rglob("*.*"))
hashes = {}

for path in paths:
    if os.path.isfile(path):
        fileText = Path(path).read_text()
        fileHash = hashlib.md5(fileText.encode())
        hashes[str(path)] = str(fileHash)

findDuplicateDictValues(hashes)
