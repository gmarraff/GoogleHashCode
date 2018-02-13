import time

def time_track(func):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        response = func(*args, **kwargs)
        print("track time --- {0} seconds --- {1}".format(time.time() - start_time, func.__name__))
        return response
    return wrapped
