'''
Slice's model
'''

class Slice:

    def __init__(self, r0, r1, c0, c1):
        self.r0, self.r1 = sorted([r0, r1])
        self.c0, self.c1 = sorted([c0, c1])

    def in_bound(self, pizza):
        return \
            self.r0 > 0 and \
            self.r1 < pizza.r and \
            self.c0 > 0 and \
            self.c1 < pizza.c

    def not_too_large(self, pizza):
        return (self.r1-self.r0+1) * (self.c1-self.c0+1) <= pizza.h

    def contain_ingredients(self, pizza):
        m = t = 0
        for row in pizza.rows[self.r0:self.r1]:
            for char in row[self.c0:self.c1]:
                if char == 'm':
                    m += 1
                else:
                    t += 1
        return (m >= self.l) and (t >= self.l)


    def is_valid(self, pizza):
        return \
            in_bound(pizza) and \
            not_too_large(pizza) and \
            contain_ingredients(pizza) # and not alreadyTaken(pizza)
