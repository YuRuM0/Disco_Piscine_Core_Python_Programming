#!/usr/bin/env python3
import sys
class methods:
    def shrink(self, string):
        print(string[:8])
    
    def enlarge(self, string):
        while (len(string) != 8):
            string += 'Z'
        print(string)
    
if (len(sys.argv) < 2):
    print("none")
else:
    for arg in sys.argv[1:]:
        a = methods()
        if (len(arg) == 8):
            print(arg)
        elif (len(arg) < 8):
            a.enlarge(arg)
        else:
            a.shrink(arg)