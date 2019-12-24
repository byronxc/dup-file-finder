#!/usr/bin/python

import sys
import os
import hashlib
from pathlib import Path



folder = "./"

if(len(sys.argv) > 1):
    folder = sys.argv[1]

paths = list(Path(folder).rglob("*.*"))
hashes = {}

for path in paths:
    if os.path.isfile(path):
        fileText = Path(path).read_text()
        fileHash = hashlib.md5(fileText.encode())
        hashes[path] = fileHash

print(hashes)
