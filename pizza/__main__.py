'''
USAGE
python main.py [-log]
PARAMS
-log for write output logs
REQUIREMENTS
python >= 3.0
colorama modules (python -m pip install colorama)
psutil modules (python -m pip install psutil)
'''
import sys
import os
import time
import psutil
from modules import parse
from modules import encode
from modules import InputError
from modules import time_track
from strategy import Solver
from strategy import Linear2DTree
from model import LinearSlice
import concurrent.futures

def solving(filename):
    try:
        # header
        print ("{0}{1}{0}".format('#' * 30, filename))

        # parsing input filename
        pizza = parse(filename)

        print ("solving cut problem for {0} file ...".format(filename))
        # solving cut algorithm
        solver = Solver(Linear2DTree())
        slice_array = solver.cut(pizza)

        # calculate slice coverage
        score = sum([slice.score for slice in slice_array])
        print ("slice coverage {0} for {1} file.".format((score)/(pizza.r*pizza.c), filename))

        # TODO: validate output

        # encoding output
        encode("output"+filename[5:-3]+".out", slice_array)
        print ("write into output{0}.out\n".format(filename[5:-3]))

        return score
    except InputError as err:
        print("Error: {0}".format(err))
    return 0

def redirect_output():
    sys.stdout = open('log/stdout_{0}.txt'.format(round(time.time() * 1000)), 'w')
    print ("# using Tree Linear algorithm")

@time_track
def main(*argv):
    # redirect file to log dir if not "-dev" arg
    if "-log" in argv: redirect_output()

    # recursion is limit to solving the last big pizza
    sys.setrecursionlimit(2 ** 20)

    # solving all pizza data sets
    input_files = [
        "input_data_set/example.in",
        "input_data_set/small.in",
        "input_data_set/medium.in",
        "input_data_set/big.in"
    ] # input_files
    size = sum([solving(input_file) for input_file in input_files])
    #with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    #    for input_file in input_files[:-1]: # no big test, too much complex
    #        try:
    #            size += executor.submit(solving(input_file)).result()
    #        except Exception as e:
    #            print ("Unexpected error: {0}\n{1}".format(e.__doc__, e.message))
    # size = sum([executor.submit(solving(input_file) for input_file in input_files[:-1]])


    # printing total score
    print ("total score: {0}".format(size))

if __name__ == "__main__":
    main(sys.argv[1:])
