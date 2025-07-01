#!/usr/bin/env python3

input = int(input("Enter a number\n"))
i = 0
while (i < 10):
    res = i * input
    print(f"{i} x {input} = {res}")
    i += 1