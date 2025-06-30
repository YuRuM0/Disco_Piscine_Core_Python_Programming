#!/usr/bin/env python3
print("Enter the first number:")
first_num = int(input())
print("Enter the second number:")
second_num = int(input())
res = first_num * second_num
print(f"{first_num} x {second_num} = {res}")
if (res > 0):
    print("The result is positive.")
elif (res == 0):
    print("The result is positive and negative.")
else:
    print("The result is negative.")