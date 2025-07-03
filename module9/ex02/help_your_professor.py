#!/usr/bin/env python3

class Average:
    def average(self, class_dict):
        res = 0
        for val in class_dict.values():
            res += val
        res = res / len(class_dict)
        return (res)

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
c = Average()
print(f"Average for class 3B: {c.average(class_3B)}.")
print(f"Average for class 3C: {c.average(class_3C)}.")