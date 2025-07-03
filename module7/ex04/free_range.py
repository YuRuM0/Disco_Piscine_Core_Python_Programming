#!/usr/bin/env python3
import sys
if (len(sys.argv) != 3):
    print("none")
elif (int(sys.argv[1]) > int(sys.argv[2])):
    print("none")
else:
    array = []
    for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        array.append(i)
    print(array)

