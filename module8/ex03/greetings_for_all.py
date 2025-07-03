#!/usr/bin/env python3

class Greetings:
    def greetings(self, message=None):
        if message is None:
            print("Hello, noble stranger.")
        elif isinstance(message, str) == True:
            print(f"Hello, {message}.")
        else:
            print("Error! It was not a name.")

g = Greetings()
g.greetings('Alexandra')
g.greetings('Wil')
g.greetings()
g.greetings(42)