#!/usr/bin/python

import sys
from pathlib import Path

folder = "./"

if(len(sys.argv) > 1):
    folder = sys.argv[1]

result = list(Path(folder).rglob("*.*"))
print(result[1])
