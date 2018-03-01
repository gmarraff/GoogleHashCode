import sys
from parser import parse


def main(argv):
    value = parse(argv[1])
    print value

if __name__ == "__main__":
    main(['', 'input/e_high_bonus.in'])
