#!/usr/bin/env python3
string = input()
i = 0
while i in range(len(string)):
    if (string[i].isupper() == True):
        print(string[i].lower(), end = "")
    elif (string[i].islower() == True):
        print(string[i].upper(), end = "")
    else:
        print(string[i], end = "")
    i += 1
print()