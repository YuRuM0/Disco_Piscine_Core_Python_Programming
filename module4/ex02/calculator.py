#!/usr/bin/env python3
num1 = int(input("Give me the first number: "))
num2 = int(input("GIve me the second number: "))
print("Thank you!")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
if (num2 == "0"):
    print("You can't divide by zero!")
else:
    print(f"{num1} / {num2} = {num1 // num2}")
print(f"{num1} * {num2} = {num1 * num2}")