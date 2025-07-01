#!/usr/bin/env python3
import sys
import re
if (len(sys.argv) != 2):
    print("none")
else:
    count = re.findall("z", sys.argv[1])
    if (len(count) == 0):
        print("none")
    else:
        print("".join(count))