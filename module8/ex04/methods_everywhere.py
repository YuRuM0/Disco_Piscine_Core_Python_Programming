#!/usr/bin/env python3
import sys
class methods:
    def shrink(string):
        print(string[:8])
    
    def enlarge(string):
        while (len(string) != 8):
            string += 'Z'
        print(string)
    
    if (len(sys.argv) < 2):
        print("none")
    for arg in sys.argv[1:]:
        if (len(arg) == 8):
            print(arg)
        elif (len(arg) < 8):
            enlarge(arg)
        else:
            shrink(arg)