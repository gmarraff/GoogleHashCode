'''
USAGE
python main.py input_path
REQUIREMENTS
python >= 3.0
'''
import sys
from models.parser import parse
from models.parser import InputError

try:
    parse(sys.argv[1])
except IndexError:
    print("Insert a file name")
except InputError as err:
    print("Error: {0}".format(err))
