#!/usr/bin/env python3

class Famous_births:
    def famous_births(self, wom_dict):
        sorted_women = sorted(wom_dict.values(), key = lambda name: name["date_of_birth"])
        for women in sorted_women:
            print(f"{women['name']} is a great scientist born in {women['date_of_birth']}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

s = Famous_births()
s.famous_births(women_scientists)