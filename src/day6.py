import numpy as np
from aocd.models import Puzzle


def solve_puzzle_one(input_array):
    sum = 0
    for g in input_array:
        s = set()
        for p in g:
            s = s.union(list(p))
        sum += len(s)
    print(sum)


def solve_puzzle_two(input_array):
    sum = 0
    for g in input_array:
        s = set()
        first = True
        for p in g:
            if first:
                s = s.union(list(p))
            else:
                s = s.intersection(list(p))
            first = False
        sum += len(s)
    print(sum)


def parse_input(data):
    return np.array([[p for p in line.split("\n")]
                     for line in data.split("\n\n")], dtype=object)


test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=6)
    if False:
        array = parse_input(test_input)
    else:
        array = parse_input(puzzle.input_data)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
