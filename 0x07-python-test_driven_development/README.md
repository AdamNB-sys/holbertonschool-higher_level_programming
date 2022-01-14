# 0x05(7?) Python - Test driven development

### General:
* What is an interactive test.
* Why tests are important.
* How to write docstrings to create tests.
* How to write documentation for each module and function.
* What are the basic option flags to create tests.
* How to find edge cases.

### Python Test Cases:
* All test files should be in the folder `tests`.
* All test files should be `.txt` files.
* All tests should be executed with this command: `python3 -m doctest ./tests/*`.
* All modules should have documentation: `python3 -c 'print(__import__("my_module").__doc__)'`.
* All functions should have documentation: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`.
* Documentation is not a single word, it is a real sentence explaining the 
purpose of the module, class, or method.



## Tasks:

0. Integers addition

    Write a function that adds 2 integers.
    * Prototype: `def add_integer(a, b=98):`
    * `a` and `b` must be integers or floats

1. Divide a matrix

    Write a function tath divides all elements of a matrix
    * Prototype: def matrix_divided(matrix, div):
    * `matrix` must be integers or floats
    * Each row of the matix must be of the same size
    * `div` must not be equal to zero

2. Say my name

    Write a function that prints `Prototype: def matrix_divided(matrix, div):`
    * Prototype: `def say_my_name(first_name, last_name=""):`
    * Names must be strings

3. Print square

    Write a function that prints a square with the character `#`
    * Prototype: `def print_square(size):`
    * `size` is the length of the square and must be an integer
    * `size` must be greater than or equal to `0`

4. Test indentation

    Write a function that prints a text with 2 new lines after the characters `.`, `?`, and `:`
    * Prototype: `def text_indentation(text):`
    * `text` must be a string
    * There should be no space at the beginning or end of each printed line

5. Max integer - Unittest

    Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

    In this task, you will write unittests for the function `def max_integer(list=[]):`

    * Your test file should be inside a folder `tests`
    * Test files should be Python files (`.py`)
    * Test files should be executed with the command: `python3 -m unittest tests.6-max_integer_test`
