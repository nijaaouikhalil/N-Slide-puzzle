import random
import time
import signal
from contextlib import contextmanager


@contextmanager
def timeout(alarm_time):
    signal.signal(signal.SIGALRM, raise_timeout)
    signal.alarm(alarm_time)
    try:
        yield
    except TimeoutError:
        pass
    finally:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)


def raise_timeout(signum, frame):
    raise TimeoutError


class TimeAnalyzer:

    def __init__(self):
        self.start = float
        self.end = float

    def start_timer(self):
        self.start = time.time()

    def end_timer(self):
        self.end = time.time()

    def get_duration(self):
        return round(self.end - self.start, 2)


def import_input(filename):
    path = "../inputs/"
    filename = filename + ".txt"
    tuples_list = []
    file = open(path+filename, 'r')
    inputs = file.readlines()
    for line in inputs:
        tuples_list.append(eval(line))
    return tuples_list


def random_puzzle(dimension):
    max_value = (dimension*dimension) + 1
    numbers = list(range(1, max_value))
    random.shuffle(numbers)
    filled_dimension = 1
    tuple_result = tuple()
    while filled_dimension <= dimension:
        inner_tuple = tuple()
        for x in range(dimension):
            inner_tuple += (numbers.pop(),)
        tuple_result += (inner_tuple,)
        filled_dimension += 1
    return tuple_result


def create_random_puzzle(dimension, number_of_puzzles, filename):
    path = "../inputs/"
    filename = filename + ".txt"
    f = open(path+filename, "w+")
    f.truncate()
    for _ in range(number_of_puzzles):
        f.write(str(random_puzzle(dimension)) + "\n")
    f.close()


if __name__ == '__main__':
    # Example to create random puzzle
    # Will be saved under /inputs directory
    # Parameters: puzzle_dimensions, number_of_puzzles, output_filename
    create_random_puzzle(6, 10, "input_tuples_6x6")
