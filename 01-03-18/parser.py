import os
global START_X, END_X
START_X = 0
START_Y = 0


class InputError(Exception):
    def __init__(self, message):
        self.message = message


def order(arr):
    return sorted(arr, key=lambda ride: abs(START_X-ride['a'])+abs(START_Y-ride['b']))


def parse(file_path):
    if not os.path.exists(file_path):
        raise InputError("Insert a valid file name")
        exit(1)
    input_file = open(file_path, "r")
    input_string = input_file.read()
    input_array = input_string.split('\n')
    r, c, f, n, b, t = input_array[0].split(' ')
    rides = input_array[1:-1]
    parsed_rides = []
    for i, ride in enumerate(rides):
        raw_ride = ride.split(' ')
        parsed_rides.append({
            'a': int(raw_ride[0]),
            'b': int(raw_ride[1]),
            'x': int(raw_ride[2]),
            'y': int(raw_ride[3]),
            's': int(raw_ride[4]),
            'f': int(raw_ride[5])
        })
    sorted_data = order(parsed_rides)
    return sorted_data
