'''
USAGE
python parser.py file_name

requirements
Python >= 3.0

valid file example:
6 7 1 5\n
TMMMTTT\n
MMMMTMM\n
TTMTTMT\n
TMMTMMM\n
TTTTTTM\n
TTTTTTM\n

'''
import os
from pizza import Pizza
class InputError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

def parse(file_path):
    if file_path is None or not os.path.exists(file_path):
        raise InputError("Insert a valid file name")
        exit(1)
    input_file = open(file_path, "r")
    input_string = input_file.read()
    input_array = input_string.split('\n')
    r, c, l, h = input_array[0].split(" ")
    if len(input_array) != int(r)+2:
        raise InputError("File is not valid, number of rows exceds spec")
        exit(1)
    rows = input_array[1:-1]
    for i, row in enumerate(rows):
        if len(row) != int(c):
            raise InputError("File is not valid, row {0} exceds spec".format(i))
            exit(1)
    return Pizza(r, c, l, h, rows)
