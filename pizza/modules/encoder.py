from .time import time_track

@time_track
def encode(out_path, slice_array):
    slice_array = sorted(slice_array,  key = lambda x: (x.r, x.c, x.area))
    ctx = str(len(slice_array)) + "\n"
    for slice in slice_array:
        if slice.is_valid():
            ctx += "{0} {1} {2} {3}\n".format(slice.r, slice.c, slice.r+slice.h-1, slice.c+slice.w-1)
    out_file = open(out_path, 'w')
    out_file.write(ctx)
