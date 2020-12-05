from math import ceil, floor

import numpy as np
from aocd.models import Puzzle


def solve_puzzle_one(input_array):
    ids = map(lambda bp: calc_id(bp, 7), input_array)
    print(max(ids))


def calc_id(bp, length_first=7):
    first = bp[0:length_first]
    sec = bp[length_first:]
    first_upper = pow(2, len(first)) - 1
    sec_upper = pow(2, len(sec)) - 1
    row = calc_id_rec(first, 0, first_upper)
    column = calc_id_rec(sec, 0, sec_upper)
    return row * 8 + column


def calc_id_rec(id, l, u):
    if len(id) == 0:
        assert (l == u)
        return l
    update = (u - l) / 2
    if id[0] == 'F' or id[0] == 'L':
        return calc_id_rec(id[1:], l, floor(u - update))
    else:
        return calc_id_rec(id[1:], ceil(l + update), u)


def solve_puzzle_two(input_array):
    ids = map(lambda bp: calc_id(bp, 7), input_array)

    sorted_ids = np.array(np.sort(list(ids)))
    missing = np.diff(sorted_ids)
    print(sorted_ids[np.argwhere(missing > 1)[0, 0]] + 1)


def parse_input(data):
    return np.array(data.splitlines())


test_input = """
FBFBBFFRLR"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=5)
    if False:
        array = parse_input(test_input)
    else:
        array = parse_input(puzzle.input_data)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
