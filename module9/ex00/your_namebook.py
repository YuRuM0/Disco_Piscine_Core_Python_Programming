#!/usr/bin/env python3

class name:
    def array_of_names(self, data):
        name_list = []
        for key, value in data.items():
            item = key.capitalize() + " " + value.capitalize()
            name_list.append(item)
        return (name_list)

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

a = name()
print(a.array_of_names(persons))