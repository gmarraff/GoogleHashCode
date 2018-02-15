from model import Linear2DSlice

def validate(slice_array):
    used = [[False for i in range(Linear2DSlice.pizza.c)] for j in range(Linear2DSlice.pizza.r)]

    for slice in slice_array:
        if slice.is_valid():
            for i in range(slice.r, slice.h):
                for j in range(slice.c, slice.w):
                    if not used[i][j]:
                        used[i][j] = True
                    else:
                        raise Exception("Solution isn't valid!")
    print ("validate solution: OK!")
    return True
