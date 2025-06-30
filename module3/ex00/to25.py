#!/usr/bin/env python3
print("Enter a number less than 25")
input = int(input())
if (input > 25):
    print("Error")
else:
    while (input < 26):
        print(f"Inside the loop, my variable is {input}")
        input += 1