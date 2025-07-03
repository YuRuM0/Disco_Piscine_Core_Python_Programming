#!/usr/bin/env python3
import numpy as np
class family_affairs:
    def find_the_redheads(self, d):
        redheads = filter(lambda name: d[name] == "red", d)
        return (list(redheads))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

fam = family_affairs()
print(fam.find_the_redheads(dupont_family))