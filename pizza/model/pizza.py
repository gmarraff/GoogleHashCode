'''
Pizza's model
'''

class Pizza:

    def __init__(self, r, c, l, h, rows):
        self.r = int(r)
        self.c = int(c)
        self.l = int(l)
        self.h = int(h)
        self.rows = rows

    def transpose(self):
        pizza.rows = list(map(list, zip(*pizza.rows)))
        pizza.r, pizza.c = pizza.c, pizza.r
