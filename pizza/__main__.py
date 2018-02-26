'''
USAGE
for the best result
python __main__.py input_data_set/example.in 1 1.0 30
python __main__.py input_data_set/small.in 1 1.0 30
python __main__.py input_data_set/medium.in 16 0.996 180
python __main__.py input_data_set/big.in 64 1 -1 1
PARAMS
-log for write output logs
REQUIREMENTS
python >= 3.0
colorama modules (python -m pip install colorama)
'''
import sys
import os
import time
from modules import parse
from modules import encode
from modules import validate
from modules import InputError
from modules import time_track
from strategy import Solver
from strategy import Linear2DTree
from model import LinearSlice
import concurrent.futures

def solving(filename, div, p, maxtime, limit):
    try:
        # header
        print ("{0}{1}{0}".format('#' * 30, filename))

        # parsing input filename
        pizza = parse(filename)

        print ("solving cut problem for {0} file ...".format(filename))
        # solving cut algorithm
        solver = Solver(Linear2DTree())
        Linear2DTree.resize_pizza(int(div))
        Linear2DTree.perc(float(p))
        Linear2DTree.set_max_time(int(maxtime))
        Linear2DTree.set_limit_upper_bound(int(limit))
        slice_array = solver.cut(pizza)

        # calculate slice coverage
        score = sum([slice.score for slice in slice_array])
        print ("slice coverage {}({}) for {} file.".format((score)/(pizza.r*pizza.c), score, filename))

        validate(slice_array)

        # encoding output
        encode("output"+filename[5:-3]+".out", slice_array)
        print ("write into output{0}.out\n".format(filename[5:-3]))

        return score
    except InputError as err:
        print("Error: {0}".format(err))
    return 0

@time_track
def main(argv):

    # recursion is limit to solving the last big pizza
    sys.setrecursionlimit(2 ** 20)
    filename = argv[1] if len(argv) > 1 else ""
    div = argv[2] if len(argv) > 2 else 1
    perc = argv[3] if len(argv) > 3 else 1.0
    maxtime = argv[4] if len(argv) > 4 else -1
    limit = argv[5] if len(argv) > 5 else 1000
    solving(filename, div, perc, maxtime, limit)

if __name__ == "__main__":
    main(sys.argv)