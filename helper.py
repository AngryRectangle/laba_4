import random
import time;


def rand_array(len, min, max):
    arr = [0] * len
    for i in range(0, len):
        arr[i] = random.randint(min, max)
    return arr


def execution_time(action):
    start = time.time()
    action()
    return time.time() - start
