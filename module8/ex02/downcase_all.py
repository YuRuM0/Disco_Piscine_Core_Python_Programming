#!/usr/bin/env python3
import sys
class downcase_it:
    def downcase_it(self, string):
        print(string.lower())

if (len(sys.argv) < 2):
    print("none")
args = sys.argv[1:]
for arg in args:
    arg = downcase_it()
    arg.downcase_it()
