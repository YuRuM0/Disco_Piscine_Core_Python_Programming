#!/usr/bin/env python3
print("Enter a number")
input = int(input())
i = 0
while (i < 10):
    res = i * input
    print(f"{i} x {input} = {res}")
    i += 1