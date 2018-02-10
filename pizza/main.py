'''
USAGE
python main.py input_path
REQUIREMENTS
python >= 3.0
'''
import sys
from modules.parser import parse
from modules.parser import InputError
from modules.solver import Solver
from modules.algorithms import Linear

def main(argv):
    try:
        pizza = parse(argv[1])
        solver = Solver(Linear())
        solver.cut(pizza)
    except IndexError:
        print("Insert a file name")
    except InputError as err:
        print("Error: {0}".format(err))

if __name__ == "__main__":
    main(sys.argv)
