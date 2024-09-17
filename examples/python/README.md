
# Main Example
================

This repository contains a simple Python program that demonstrates the use of classes to create custom greeting and farewell messages. The program consists of two files: `main_example.py` and `classes.py`.

## main_example.py
-----------------

The `main_example.py` file serves as the entry point for the program. It defines a `main` function that prompts the user to enter their name, creates instances of the `Greeting` and `Farewell` classes with the provided name, and then prints out the resulting greeting and farewell messages.

### Usage
-----

To run the program, simply execute the `main_example.py` file using Python. For example:
```
$ python main_example.py
Enter your name: John
Hello, John!
Goodbye, John!
```
## classes.py
----------------

The `classes.py` file defines the `Greeting` and `Farewell` classes, which are responsible for generating the greeting and farewell messages.

### Greeting Class
--------------

The `Greeting` class has the following methods:

* `__init__(name)`: Initializes the class with the provided name.
* `say_hello()`: Returns a greeting message using the provided name.

### Farewell Class
--------------

The `Farewell` class has the following methods:

* `__init__(name)`: Initializes the class with the provided name.
* `say_goodbye()`: Returns a farewell message using the provided name.

### Usage
-----

To use these classes in your own program, you can import them from the `classes` module and create instances as needed. For example:
```
from classes import Greeting, Farewell

greeting = Greeting("John")
print(greeting.say_hello())  # Output: "Hello, John!"

farewell = Farewell("Jane")
print(farewell.say_goodbye())  # Output: "Goodbye, Jane!"
```
## Contributing
--------------

If you'd like to contribute to this project, please feel free to submit a pull request or open an issue. If you have any questions or need help with the code, don't hesitate to reach out.

## License
---------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

This readme file was auto-generated using Readme Genie