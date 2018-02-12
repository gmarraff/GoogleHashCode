def encode(out_path, slice_array):
    ctx = str(len(slice_array)) + "\n"
    for slice in slice_array:
        ctx += "{0} {1} {2} {3}\n".format(slice.r, slice.c, slice.r, slice.c+slice.size-1)
    out_file = open(out_path, 'w')
    out_file.write(ctx)
