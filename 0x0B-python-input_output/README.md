# 0x0B Python - Input/Output


## General
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor line in a file
* How to make sure a file is closed after using it
* What is and how to use the `with` statement
* What is `JSON`
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

## Tasks

0. Read file

    Write a function that reads a text file (`UTF8`) and prints it to stdout:
    * Prototype: `def read_file(filename=""):`

1. Write to a file

    Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:
    * Prototype: `def write_file(filename="", text=""):`

2. Append to a file

    Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:
    * Prototype: `def append_write(filename="", text=""):`

3. To JSON string

    Write a function that returns the JSON representation of an object (string):
    * Prototype: `def to_json_string(my_obj):`

4. From JSON string to Object

    Write a function that returns an object (Python data structure) represented by a JSON string:
    * Prototype: `def from_json_string(my_str):`

5. Save object to a file

    Write a function that writes an Object to a text file, using a JSON representation:
    * Prototype: `def save_to_json_file(my_obj, filename):`

6. Create object from JSON file

    Write a function that creates an Object from a “JSON file”:
    * Prototype: `def load_from_json_file(filename):`

7. Load, add, save

    Write a script that adds all arguments to a Python list, and then save them to a file:
    * You must use your function `save_to_json_file` from `5-save_to_json_file.py`
    * You must use your function `load_from_json_file` from `6-load_from_json_file.py`
    * The list must be saved as a JSON representation in a file named `add_item.json`

8. Class to JSON

    Write a function that returns the dictionary description with simple data 
    structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
    * Prototype: `def class_to_json(obj):`
    * `obj` is an instance of a Class
    * All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean

9. Student to JSON

    Write a class `Student` that defines a student by:
    * Public instance attributes:
        * `first_name`
        * `last_name`
        * `age`
    * Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
    * Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance 
    (same as `8-class_to_json.py`)

10. Student to JSON with filter

    Write a class `Student` that defines a student by:
    * Public instance attributes:
        * `first_name`
        * `last_name`
        * `age`
    * Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
    * Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
        * If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
        * Otherwise, all attributes must be retrieved

11. Student to disk reload

    Write a class `Student` that defines a student by:
    * Public instance attributes:
        * `first_name`
        * `last_name`
        * `age`
    * Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
    * Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
        * If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
        * Otherwise, all attributes must be retrieved
    * Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
        * You can assume `json` will always be a dictionary
        * A dictionary key will be the public attribute name
        * A dictionary value will be the value of the public attribute

12. Pascals triangle

    Technical interview preparation:
    * You are not allowed to google anything
    * Whiteboard first

    Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
    * Returns an empty list if `n <= 0`
    * You can assume `n` will be always an integer
    * You are not allowed to import any module