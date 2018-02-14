'''
Slice's model

REQUIREMENTS:
python -m pip install colorama
'''
import colorama
import functools

class LinearSlice:
    pizza = None

    def __init__(self, r, c):
        if LinearSlice.pizza is None:
            raise Exception("pizza not initialized with correct static method")

        self.r = int(r)
        if self.r < 0 or self.r >= LinearSlice.pizza.r:
            raise Exception("first param (r) not in pizza's bound")

        self.c = int(c)
        if self.c < 0 or self.c >= LinearSlice.pizza.c:
            raise Exception("second param (c) not in pizza's bound")

        self.size = 1

        self.t = 1 if LinearSlice.pizza.rows[r][c] is 'T' else 0
        self.m = 1 if LinearSlice.pizza.rows[r][c] is 'M' else 0


    def static_init(pizza):
        colorama.init()
        LinearSlice.pizza = pizza

    def contain_ingredients(self):
        return \
            min(self.m, self.t) >= LinearSlice.pizza.l and \
            self.size <= LinearSlice.pizza.h

    def in_bound(self):
        return self.c + self.size <= LinearSlice.pizza.c

    def not_in_bound(self):
        return not self.in_bound()

    def too_large(self, i=0):
        return self.size+i > LinearSlice.pizza.h

    def not_too_large(self, i=0):
        return not self.too_large(i)

    def add_right(self):
        if self.size < LinearSlice.pizza.h and self.c+self.size < LinearSlice.pizza.c:
            self.t += 1 if LinearSlice.pizza.rows[self.r][self.c+self.size] is 'T' else 0
            self.m += 1 if LinearSlice.pizza.rows[self.r][self.c+self.size] is 'M' else 0
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
        c_start = '\033[91m' if self.size > LinearSlice.pizza.h else "\033[0m"
        c_end = '\033[0m'
        return str(c_start+"(r:{0}, c:{1}, size:{2})"+c_end).format(self.r, self.c, self.size)

    def __eq__(self, other):
        return isinstance(self, other.__class__) and self.__dict__ == other.__dict__

class AntiLinearSlice(LinearSlice):

    def __init__(self, r, c):
        super().__init__(r, c)

    # unsafe
    def add_rigth(self):
        if self.c+self.size < LinearSlice.pizza.c:
            self.t += 1 if LinearSlice.pizza.rows[self.r][self.c+self.size] is 'T' else 0
            self.m += 1 if LinearSlice.pizza.rows[self.r][self.c+self.size] is 'M' else 0
        self.size += 1

class Linear2DSlice():

    pizza = None

    def static_init(pizza):
        colorama.init()
        Linear2DSlice.pizza = pizza

    @functools.lru_cache(maxsize=None) # unbounded
    def create(r, c, h, w):
        return Linear2DSlice(r, c, h, w)

    def __init__(self, r, c, h, w):
        if Linear2DSlice.pizza is None:
            raise Exception("pizza not initialized with correct static method")

        self.r, self.c, self.h, self.w = r, c, h, w
        self.area = self.h * self.w
        self.m = self.t = 0
        self.v = self.__condition()
        if self.v:
            self.__ci()
            self.score = self.area if self.is_valid() else 0
        else:
            self.score = 0

    def is_valid(self):
        return self.v and min(self.m, self.t) >= Linear2DSlice.pizza.l

    def __condition(self):
        return \
            min(self.r, self.c) >= 0 and \
            self.r < Linear2DSlice.pizza.r and \
            self.c < Linear2DSlice.pizza.c and \
            self.area <= Linear2DSlice.pizza.h and \
            min(self.w, self.h) > 0 and \
            self.r+self.h <= Linear2DSlice.pizza.r and \
            self.c+self.w <= Linear2DSlice.pizza.c

    def __ci(self, lower_bound =0):
        for i in range(self.r, self.r+self.h):
            for j in range(self.c + lower_bound, self.c+self.w):
                if Linear2DSlice.pizza.rows[i][j] is 'M':
                    self.m += 1
                else:
                    self.t += 1

    def add_right(self):
        old_w = self.w
        self.w += 1
        self.area += self.h
        self.v = self.__condition()
        if self.v:
            self.__ci(old_w)
            self.score = self.area
        else:
            self.score = 0
        return self

    def __str__(self):
        c_start = '\033[91m' if not self.is_valid() else "\033[0m"
        c_end = '\033[0m'
        return str(c_start+"(r:{0}, c:{1}, h:{2}, w:{3}, area:{4}, score:{5}, m:{6}, t:{7})"+c_end).format(self.r, self.c, self.h, self.w, self.area, self.score, self.m, self.t)

    def __eq__(self, other):
        return isinstance(self, other.__class__) and self.__dict__ == other.__dict__

    def __lt__(self, other):
        return isinstance(self, other.__class__) and (self.r < other.r and self.c < other.c)

    # make it hashable
    def __hash__(self):
        return hash(repr(self))
