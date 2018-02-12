import time

def time_track(msg, fun, *args):
    start_time = time.time()
    out = fun(*args)
    print("track time --- {0} seconds --- {1}".format(time.time() - start_time, msg))
    return out
