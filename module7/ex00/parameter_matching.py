#!/usr/bin/env python3
import sys
key = "Bonjour"
if (len(sys.argv)!= 2):
    print("none")
elif (key == sys.argv[1]):
    print(f"What was the parameter? {key}")
    print("Good job!")
else:
    print(f"What was the parameter? {key}")
    print("Nope, sorry...")
