'''
USAGE
python main.py input_path
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
from strategy import Linear
from strategy import LinearTree
from model import LinearSlice

def solving(filename):
    out = 0
    try:
        print ('#' * 60)
        pizza = time_track("parsing {0}".format(filename), parse, filename)
        pizza.rows = list(map(list, zip(*pizza.rows)))
        temp = pizza.r
        pizza.r=pizza.c
        pizza.c=temp
        print ("solving cut problem for {0} file ...".format(filename))
        solver = Solver(LinearTree())
        slice_array = time_track("solving {0}".format(filename), solver.cut, pizza)
        size = 0
        for slice in slice_array:
            size += slice.size
        print ("slice coverage {0} for {1} file.".format((size)/(pizza.r*pizza.c), filename))
        time_track("encoding output{0}.out".format(filename[5:-3]), encode, "output"+filename[5:-3]+".out", slice_array,)
        print ("write into output{0}.out\n".format(filename[5:-3]))
        out = size
    except InputError as err:
        print("Error: {0}".format(err))
    return out

def main(*argv):
    size = 0
    size += solving("input_data_set/example.in")
    size += solving("input_data_set/small.in")
    size += solving("input_data_set/medium.in")
    size += solving("input_data_set/big.in")
    print ("total score: {0}".format(size))

def getCurrentMemoryUsage():
    # Memory usage in kB
    f = open('/proc/{}/status'.format(os.getpid()))
    memusage = int(f.read().split('VmRSS:')[1].split('\n')[0][:-3].strip())
    f.close()
    return memusage

if __name__ == "__main__":
    orig_stdout = sys.stdout
    f = open('log/stdout_{0}.txt'.format(round(time.time() * 1000)), 'w')
    sys.stdout = f
    print ("# using Tree Linear algorithm with transposed pizza")
    sys.setrecursionlimit(2 ** 20)
    time_track("main", main)
    print ("# using {0} [MB] of memory".format(getCurrentMemoryUsage()))
    sys.stdout = orig_stdout
    f.close()
