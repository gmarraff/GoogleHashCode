'''
USAGE
python main.py input_path
REQUIREMENTS
python >= 3.0
'''

import time
from modules import parse
from modules import InputError
from strategy import Solver
from strategy import Linear

def solving(filename):
    out = 0
    try:
        pizza = parse(filename)
        solver = Solver(Linear())
        slice_array = solver.cut(pizza)
        size = 0
        for slice_in_line in slice_array:
            for slice in slice_in_line:
                size += slice.size
        print ("slice coverage {0} for {1} file.".format((size)/(pizza.r*pizza.c), filename))
        out = size
    except IndexError:
        print("Insert file name")
    except InputError as err:
        print("Error: {0}".format(err))
    return out

def main():
    size = solving("input_data_set/example.in")
    size += solving("input_data_set/small.in")
    size += solving("input_data_set/medium.in")
    size += solving("input_data_set/big.in")
    print ("total score: {0}".format(size))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
