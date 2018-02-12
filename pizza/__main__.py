'''
USAGE
python main.py input_path
REQUIREMENTS
python >= 3.0
colorama modules (python -m pip install colorama)
'''
import sys
import time
from modules import parse
from modules import encode
from modules import InputError
from modules import time_track
from strategy import Solver
from strategy import Linear
from model import LinearSlice

def solving(filename):
    out = 0
    try:
        print ('#' * 60)
        pizza = time_track("parsing {0}".format(filename), parse, filename)
        print ("solving cut problem for {0} file ...".format(filename))
        solver = Solver(Linear())
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
    size = solving("input_data_set/example.in")
    size += solving("input_data_set/small.in")
    size += solving("input_data_set/medium.in")
    size += solving("input_data_set/big.in")
    print ("total score: {0}".format(size))

if __name__ == "__main__":
    orig_stdout = sys.stdout
    f = open('/log/stdout_{0}.txt'.format(round(time.time() * 1000)), 'w')
    sys.stdout = f
    print ("# using Linear algorithm")
    time_track("main", main)
    sys.stdout = orig_stdout
    f.close()
