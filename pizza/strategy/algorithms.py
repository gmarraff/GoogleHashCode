from .engine import Engine
from model import Pizza
from model import LinearSlice
from model import AntiLinearSlice
from modules import time_track
from modules import DotDict
import functools
from collections import deque
from model import Linear2DSlice

class Linear(Engine):

    def algorithm(self, pizza):
        LinearSlice.static_init(pizza)
        out = []
        anti = []
        for i in range(0, pizza.r):
            call = self.linear(i, pizza.c)
            out.append(call[0])
            anti.append(call[1])

        return [item for sublist in out for item in sublist]

    def linear(self, index, upper):
        array_slices = []
        array_anti = []
        i = 0
        while i < upper:
            slice, anti, i = self.add_slice(index, i)
            if slice is not None:
                array_slices.append(slice)
            elif anti is not None and len(array_anti) > 0 and array_anti[-1].c+array_anti[-1].size-1 is i - 2:
                array_anti[-1].add_right()
            else:
                array_anti.append(anti)

        return array_slices, array_anti

    def add_slice(self, i, j):
        slice = LinearSlice(i, j)
        counter = j + 1
        while \
            slice.is_not_valid() and \
            slice.add_right():
            counter += 1
        if slice.is_valid():
            return slice, None, counter
        else:
            return None, AntiLinearSlice(i, j), j + 1

class LinearTree(Engine):

    i=0

    def algorithm(self, pizza):
        LinearSlice.static_init(pizza)
        out = []
        for index in range(0, pizza.r):
            LinearTree.i = index
            self.tree_row.cache_clear()
            out.append(self.tree_row(0)[0])
        return [item for sublist in out for item in sublist]

    @functools.lru_cache(maxsize=None)
    def tree_row(self, i, j):
        # caso base non ho spazio nemmeno per la slice di lunghezza minore
        if j > LinearSlice.pizza.c-(LinearSlice.pizza.l*2):
            return [], 0
        maxSize = 0
        # slices[i] contiene la lista contenente la fetta trovata nell'i-esima ricorsione unita
        # a le fette che massimizzano il punteggio, nella row in questione, da j+fetta.size in poi
        slices = []
        for l in range(min(LinearSlice.pizza.c-j, LinearSlice.pizza.h), LinearSlice.pizza.l*2, -1):
            # creo la fetta di dimensione l
            slice = self.add_slice(j, l)
            #print ("j: {0}, l: {1}, slice: {2}, min: {3}".format(j, l, slice, min(LinearSlice.pizza.c-j, LinearSlice.pizza.h)))
            # ritorno la lista che massimizza il resto della row e il suo valore di size
            if slice is not None:
                recursive = self.tree_row(j+l)
                size = slice.size + recursive[1]
            else:
                recursive = self.tree_row(j+1)
                size = recursive[1]
            if size > maxSize:
                slices = []
                # controllo se la fetta creata è corretta
                if slice is not None: # aggiungo a slices la lista contenente la fetta creata seguita dalla lista ritornata
                    # dalla chiamata ricorsiva
                    slices.append(slice)
                    maxSize = slice.size + recursive[1]
                else:
                    maxSize = recursive[1]
                for sl in recursive[0]:
                    slices.append(sl)
        return slices, maxSize

    def add_slice(self, i, j, l):
        slice = LinearSlice(i, j)
        while \
            slice.size is not l and \
            slice.add_right():
            pass
        return slice if slice.is_valid() and slice.size is l else None

class Linear2DTree(Engine):

    H = L = C = R = 0
    ROWS = None

    def algorithm(self, pizza):
        # init LinearSlice
        Linear2DSlice.static_init(pizza)

        # init static const
        Linear2DTree.H, \
        Linear2DTree.L, \
        Linear2DTree.C, \
        Linear2DTree.R, \
        Linear2DTree.ROWS = \
        Linear2DSlice.pizza.h, \
        Linear2DSlice.pizza.l, \
        Linear2DSlice.pizza.c, \
        Linear2DSlice.pizza.r, \
        Linear2DSlice.pizza.rows

        return list(self.big_slice(0, Linear2DTree.R, 0).list)

    '''
    DESC
    compute sub-problem (_0) ROWS[i:j][k:],
    divide-et-impera solution in max(z) sub problems:
    (_1) ROWS[i:z][k:] and (_2) ROWS[z+1:j][k:]
    for each z in [i+1, j] => max(z) = j-i-1
    base case: (_0)'s area is minor or equal then H
    resolving (_1) with big_slice_solver(i, z, k)
    resolving (_2) with recursive call (z+1, j, k)
    sum of this two problem's solution
    and search the best, for each z, to resolving (_0)
    PARAMS
    i: int, first row of sub-problem
    j: int, last row of sub-problem
    k: int, first column of sub-problem
    RETURNS
    .list, contain a list of slice that maximize the score of sub-problem
    .score, the best score for the sub-problem
    COMPLEXITY O(...) with memoized cache
    '''
    # TODO: implements right limit
    @functools.lru_cache(maxsize=None) # unbounded
    def big_slice(self, i, j, k):
        # return DotDict({'list': deque(), 'score': 0}) # mock
        height = j-i+1
        # base case
        _all = Linear2DSlice.create(i, k, height, Linear2DTree.C-k)
        if _all.area <= Linear2DTree.H: return \
            DotDict({'list': deque([_all]), 'score': _all.score}) \
            if _all.is_valid() else DotDict({'list': deque(), 'score': 0})

        upper_bound = min(i+Linear2DTree.H, j+1)

        # init output returns
        # key value accessing by dot
        local_best = DotDict({'list': deque(), 'score': 0})

        # calculate big_slice problem
        for z in range(i, upper_bound):
            # recursive and big slice solver call
            # FIXME: who call first for performance improvments?
            recursive_call = self.big_slice(z+1, j, k)
            slice_solver = self.big_slice_solver(i, z, k)

            # calculating score of this test
            local_score = recursive_call.score + slice_solver.score

            # check if test score is better
            if local_score > local_best.score:
                # refresh best case
                local_best.list = deque(set().union(slice_solver.list, recursive_call.list))
                local_best.score = local_score

        return local_best
        # big_slice close

    '''
    DESC
    compute sub-problem (_0) ROWS[i:j][k:],
    divide-et-impera solution in max(max_weight) sub problems:
    (_1) ROWS[i:j][k:z] and (_2) ROWS[i:j][z+1:]
    for each z in [k, k+max_weight]
    with max_weight = H // (j-i)
    base case: (_0)'s area is minor or equal then H
    resolving (_1) with max fit valid slice of length z
    resolving (_2) with big_slice(i, j, k+z)
    sum of this two problem's solution
    and search the best, for each z, to resolving (_0)
    PARAMS
    i: int, first row of sub-problem
    j: int, last row of sub-problem
    k: int, first column of sub-problem
    RETURNS
    .list, contain a list of slice that maximize the score of sub-problem
    .score, the best score for the sub-problem
    COMPLEXITY O(...) with memoized cache
    '''
    @functools.lru_cache(maxsize=None) # unbounded
    def big_slice_solver(self, i, j, k):
        # return DotDict({'list': deque(), 'score': 0}) # mock
        # height is fixed for every slice in this function
        height = j-i+1
        # base case
        _all = Linear2DSlice.create(i, k, height, Linear2DTree.C-k)
        if _all.area <= Linear2DTree.H:return \
            DotDict({'list': deque([_all]), 'score': _all.score}) \
            if _all.is_valid() else DotDict({'list': deque(), 'score': 0})

        # weights = reversed([w+1 for w, _ in enumerate(range(height, Linear2DTree.H, height))])
        weights = [w+1 for w, _ in enumerate(range(height, Linear2DTree.H+1, height))]

        # init output returns
        # key value accessing by dot
        local_best = DotDict({'list': deque(), 'score': 0})
        first_time = True
        for weight in weights:
            '''
            if first_time:
                # increasing performance with add_right in Linear2DSlice
                local_slice = Linear2DSlice.create(i, k, height, weight)
                first_time = False
            else:
                local_slice.add_right()
            '''
            local_slice = Linear2DSlice.create(i, k, height, weight)

            big_slice_rec = self.big_slice(i, j, k+weight)

            # calculating score of this test
            local_score = local_slice.score + big_slice_rec.score

            # check if test score is better
            if local_score > local_best.score:
                # refresh best case
                local_best.list = deque(set().union([local_slice], big_slice_rec.list))
                local_best.score = local_score

        return local_best

        # big_slice_solver close
