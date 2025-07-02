#!/usr/bin/env python3

class greetings:
    def greetings(message = 'Hello, noble stranger'):
        if isinstance(message, str):
            print(f"Hello, {message}.")
        else:
            print("Error! It was not a name.")
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)