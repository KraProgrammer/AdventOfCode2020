import numpy as np
from aocd.models import Puzzle


def solve_puzzle_one(data):
    memory = [0] * 2020

    for idx, value in enumerate(data[:-1]):
        memory[value] = idx + 1

    prev = data[-1]
    curr = -1
    for i in range(len(data), 2020):
        curr = i - memory[prev]
        if curr == i:
            curr = 0
        memory[prev] = i
        prev = curr

    print(curr)


def solve_puzzle_two(data):
    memory = [0] * 30000000

    for idx, value in enumerate(data[:-1]):
        memory[value] = idx + 1

    prev = data[-1]
    curr = -1
    for i in range(len(data), 30000000):
        curr = i - memory[prev]
        if curr == i:
            curr = 0
        memory[prev] = i
        prev = curr

    print(curr)


def parse_input(data):
    return np.fromstring(data, dtype=int, sep=',')


test_input = """1,3,2
"""

test_input2 = """2,1,3"""
test_input0 = """0,3,6"""
test_input6 = """3,1,2"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=15)
    if False:
        array = parse_input(test_input6)
    else:
        array = parse_input(puzzle.input_data)
    print(array)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
