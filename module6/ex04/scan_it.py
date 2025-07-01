#!/usr/bin/env python3
import re
import sys
if (len(sys.argv) != 3):
    print("none")
else:
    key = sys.argv[1]
    res = re.findall(key, sys.argv[2])
    print(len(res))