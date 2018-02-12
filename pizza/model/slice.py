'''
Slice's model

REQUIREMENTS:
python -m pip install colorama
'''
import colorama

class LinearSlice:
    __pizza = None

    def __init__(self, r, c):
        if LinearSlice.__pizza is None:
            raise Exception("pizza not initialized with correct static method")

        self.r = int(r)
        if self.r < 0 or self.r >= LinearSlice.__pizza.r:
            raise Exception("first param (r) not in pizza's bound")

        self.c = int(c)
        if self.c < 0 or self.c >= LinearSlice.__pizza.c:
            raise Exception("second param (c) not in pizza's bound")

        self.size = 1

        self.t = 1 if LinearSlice.__pizza.rows[r][c] is 'T' else 0
        self.m = 1 if LinearSlice.__pizza.rows[r][c] is 'M' else 0


    def static_init(pizza):
        colorama.init()
        LinearSlice.__pizza = pizza

    def contain_ingredients(self):
        return \
            min(self.m, self.t) >= LinearSlice.__pizza.l and \
            self.size <= LinearSlice.__pizza.h

    def in_bound(self):
        return self.c + self.size <= LinearSlice.__pizza.c

    def not_in_bound(self):
        return not self.in_bound()

    def too_large(self, i=0):
        return self.size+i > LinearSlice.__pizza.h

    def not_too_large(self, i=0):
        return not self.too_large(i)

    def add_right(self):
        if self.size < LinearSlice.__pizza.h and self.c+self.size < LinearSlice.__pizza.c:
            self.t += 1 if LinearSlice.__pizza.rows[self.r][self.c+self.size] is 'T' else 0
            self.m += 1 if LinearSlice.__pizza.rows[self.r][self.c+self.size] is 'M' else 0
            self.size += 1
            return True
        else:
            return False

    def is_valid(self):
        return \
            self.in_bound() and \
            self.not_too_large() and \
            self.contain_ingredients()

    def is_not_valid(self):
        return not self.is_valid()

    def __str__(self):

        c_start = '\033[91m' if self.size > LinearSlice.__pizza.h else "\033[0m"
        c_end = '\033[0m'
        return str(c_start+"(r:{0}, c:{1}, size:{2})"+c_end).format(self.r, self.c, self.size)

    def __eq__(self, other):
        return isinstance(self, other.__class__) and self.__dict__ == other.__dict__

class AntiLinearSlice(LinearSlice):

    def __init__(self, r, c):
        super().__init__(r, c)

    # unsafe
    def add_rigth(self):
        if self.c+self.size < LinearSlice.__pizza.c:
            self.t += 1 if LinearSlice.__pizza.rows[self.r][self.c+self.size] is 'T' else 0
            self.m += 1 if LinearSlice.__pizza.rows[self.r][self.c+self.size] is 'M' else 0
        self.size += 1
