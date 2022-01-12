0x04 Python - Classes and Objects

General:
* What is OOP
* "first-class everything"
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected, and private attributes
* What is `self`
* What is a method
* What is the special `__init__` method and how to use it
* What is data abstraction, data encapsulation, and information hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to objects and classes
* What is the `__dict__` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function



Tasks:

0. Square with size

    Write a class `Square` that defines a square by:
    * Private instance attribute: `size`
    * Instantiation with `size`

    Why?

    Why is `size` a private attribute?

1. Size validation

    Write a class `Square` that defines a square by:
    * Private instance attribute: `size`
    * Instantiation with optional `size`: `def __init__(self, size=0):`
        * `size` must be integer
        * if `size` is less that 0, raise a value error

2. Area of a square

    Write a class `Square` that defines a square by:
    * Private instance attribute: `size`
    * instantiation with optional `size`: `def __init__(self, size=0):`
        * `size` must be integer
        * if `size` is less that 0, raise a value error

3. Access and update private attribute

    Write a class `Square` that definites a square by:
    * Private instance attribute: `size`
        * property `def size(self):` to retrieve it
        * property setter `def size(self, value):` to set it
            * `size` must be an integer
            * if `size` is less that 0, raise a value error
    * Instantiation with optional `size`: `def __init__(self, size=0):`
    * Public instance method: `def area(self):` that returns the current square area

4. Printing a square

    Write a class `Square` that definites a square by:
    * Private instance attribute: `size`
        * property `def size(self):` to retrieve it
        * property setter `def size(self, value):` to set it
            * `size` must be an integer
            * if `size` is less that 0, raise a value error
    * Instantiation with optional `size`: `def __init__(self, size=0):`
    * Public instance method: `def area(self):` that returns the current square area
    * Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
        * if `size` is equal to 0, print an empty line
