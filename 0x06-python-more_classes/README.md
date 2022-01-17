# 0x06 Python - More Classes and Objects

## General: 

* What is the special `__init__` method and how to use it
* What are the special `__str__` and `__repr__` methods and how to use them
* What is the difference between `__str__` and `__repr__`
* What is a class attribute
* What is the difference betweeen an object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to objects and classes
* What is and what does the `__dict__` of a class or instance contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (memory address in CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions

---

## Tasks:

0. Real definition of a rectangle

    Write a class `Rectangle` that definies a rectangle by:
    * Private instance attribute: `width`
        * property `def width(self):` to retrieve it
        * property setter `def width(self, value):` to set it
    * Private instance of attribute: `height`
        * property `def height(self):` to retrieve it
    * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
---

1. Area and Perimeter

    Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)
    * Private instance attribute: `width`
        * property `def width(self):` to retrieve it
        * property setter `def width(self, value):` to set it
    * Private instance attribute: `height`
        * property `def height(self):` to retrieve it
        * property setter `def height(self, value):`
    * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
    * Public instance method: `def area(self):` that returns the rectangle area
    * Public instance method: `def perimeter(self):` that returns the rectangle perimeter
        * if `width` or `height` is equal to 0, perimeter is 0
---

2. String representation

    Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)
    * Private instance attribute: `width`
        * property `def width(self):` to retrieve it
        * property setter `def width(self, value):` to set it
    * Private instance attribute: `height`
        * property `def height(self):` to retrieve it
        * property setter `def height(self, value):`
    * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
    * Public instance method: `def area(self):` that returns the rectangle area
    * Public instance method: `def perimeter(self):` that returns the rectangle perimeter
        * if `width` or `height` is equal to 0, perimeter is 0
    * `print()` and `str()` should print the rectangle with the character `#`:
        * if `width` or `height` is equal to 0, return an empty string
---

3. Eval is magic

    Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)
    * Private instance attribute: `width`
        * property `def width(self):` to retrieve it
        * property setter `def width(self, value):` to set it
    * Private instance attribute: `height`
        * property `def height(self):` to retrieve it
        * property setter `def height(self, value):`
    * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
    * Public instance method: `def area(self):` that returns the rectangle area
    * Public instance method: `def perimeter(self):` that returns the rectangle perimeter
        * if `width` or `height` is equal to 0, perimeter is 0
    * `print()` and `str()` should print the rectangle with the character `#`:
        * if `width` or `height` is equal to 0, return an empty string
    * `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
---
