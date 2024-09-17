# classes.py

class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}!"

class Farewell:
    def __init__(self, name):
        self.name = name

    def say_goodbye(self):
        return f"Goodbye, {self.name}!"
