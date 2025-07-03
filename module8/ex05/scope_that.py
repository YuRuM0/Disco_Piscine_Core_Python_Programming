#!/usr/bin/env python3

class scope:
    def add_one(self, param):
        param += 1
        return (param)

s = scope()
var = 5
print(var)
s.add_one(var)
print(var)


