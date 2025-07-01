#!/usr/bin/env python3
import sys
if (len(sys.argv) < 2):
    print("none")
else:
    args = sys.argv[1:]
    for arg in args:
        if (arg.find("ism") == -1): #when value not found, returns -1
            print(arg + "ism")
        else:
            print(arg)