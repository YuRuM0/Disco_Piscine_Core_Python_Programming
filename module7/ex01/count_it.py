#!/usr/bin/env python3
import sys
if (len(sys.argv) < 2):
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    args = sys.argv[1:]
    for arg in args:
        print(f"{arg}: {len(arg)}")