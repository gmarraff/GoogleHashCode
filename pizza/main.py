'''
USAGE
python main.py input_path
REQUIREMENTS
python >= 3.0
'''
import sys
import time
from modules.parser import parse
from modules.parser import InputError
from modules.solver import Solver
from modules.algorithms import Linear

def main(argv):
    try:
        pizza = parse(argv[1])
        solver = Solver(Linear())
        slice_array = solver.cut(pizza)
        size = 0
        for slice_in_line in slice_array:
            for slice in slice_in_line:
                size += slice.size
        print ("slice coverage {0}%".format((size*100)/(pizza.r*pizza.c)))
    except IndexError:
        print("Insert file name")
    except InputError as err:
        print("Error: {0}".format(err))

if __name__ == "__main__":
    start_time = time.time()
    main(sys.argv)
    print("--- %s seconds ---" % (time.time() - start_time))
