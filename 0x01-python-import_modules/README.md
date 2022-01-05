0x01 Python - import & modules

General:
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs
* What's the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What's the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception


Tasks:

0. Import a simple function from a simple file.

    Write a proram that imports the function `def add(a, b)` from the file
    `add_0.py` and prints the result of the addition `1 + 2 = 3`.
    * You have to use the `print` function with string format to display
    integers

1. How to make a script dynamic.

    Write a program that prints the number of and the list of its arguments.

2. Everything can be imported.

    Write a program that imports the variable `a` from the file 
    `variable_load_2.py` and prints its value.
    * You are not allowed to use the `*` for importing or `__import`
    * Your code should not be executed when imported

3. Integers division with debug.

    Write a function that divides 2 integers and prints the result.
    * Prototype: `def safe_print_division(a, b):`

4. Raise exception.

    Write a function that raises a type exception
    * Prototype: `def raise_exception():`

5. Raise a message.

    Write a function that raises a name exception with a message
    * Prototype: `def raise_exception_msg(message=""):`

Quiz:
0. B
1. C
2. C
3. A
4. B
5. C