#!/usr/bin/env python3
orig_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
i = 0
while (i in range(len(orig_array))):
    new_array.append(orig_array[i] + 2)
    i += 1
print(f"Original array: {orig_array}")
print(f"New array: {new_array}")