#!/usr/bin/env python3
orig_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
i = 0
while (i in range(len(orig_array))):
    if (orig_array[i] > 5):
        new_array.append(orig_array[i] + 2)
    i += 1
print(orig_array)
print(new_array)