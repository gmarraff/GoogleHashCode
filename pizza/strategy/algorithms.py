from .engine import Engine
from model import Pizza
from model import LinearSlice
from model import AntiLinearSlice
from modules import time_track

import functools

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
    def tree_row(self, j):
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


    def add_slice(self, j, l):
        slice = LinearSlice(LinearTree.i, j)
        while \
            slice.size is not l and \
            slice.add_right():
            pass
        return slice if slice.is_valid() and slice.size is l else None
