from itertools import product

import numpy as np
from aocd.models import Puzzle


def solve_puzzle_one(input_array):
    for val1 in input_array:
        for val2 in input_array:
            if val1 + val2 == 2020:
                print(val1 * val2)


def solve_puzzle_two(input_array):
    for v1, v2, v3 in product(input_array, input_array, input_array):
        if v1 + v2 + v3 == 2020:
            print(v1 * v2 * v3)


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=1)
    array = np.fromstring(puzzle.input_data, dtype=int, sep='\n')
    solve_puzzle_one(array)
    solve_puzzle_two(array)
