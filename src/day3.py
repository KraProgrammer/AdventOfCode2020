import numpy as np
from aocd.models import Puzzle


def solve_puzzle_one(input_array):
    print(count_t(input_array, 1, 3))


def count_t(arr, d, r):
    x = 0
    y = 0
    t = 0
    while x + d < len(arr):
        x += d
        y += r
        if arr[x][y % len(arr[x])] == '#':
            t += 1
    return t


def solve_puzzle_two(input_array):
    c = count_t(input_array, 1, 1) \
        * count_t(input_array, 1, 3) \
        * count_t(input_array, 1, 5) \
        * count_t(input_array, 1, 7) \
        * count_t(input_array, 2, 1)
    print(c)


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=3)
    array = np.array(puzzle.input_data.splitlines())
    solve_puzzle_one(array)
    solve_puzzle_two(array)
