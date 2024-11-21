# main_example.py

from classes import Farewell, Greeting


def main():
    name = input("Enter your name: ")

    greeting = Greeting(name)
    farewell = Farewell(name)

    print(greeting.say_hello())
    print(farewell.say_goodbye())


if __name__ == "__main__":
    main()
