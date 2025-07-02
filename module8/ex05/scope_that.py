#!/usr/bin/env python3

class scope:
    def add_one(param):
        param += 1
    
    var = 10
    print(var)
    add_one(var) # or var = add_one(var)?
    print(var)


