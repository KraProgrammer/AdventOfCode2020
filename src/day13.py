from functools import reduce

import numpy as np
from aocd.models import Puzzle


def solve_puzzle_one(minutes, input_array):
    next = get_next(input_array, minutes)
    index_min = np.argmin(next)
    print(input_array[index_min] * (next[index_min] - minutes))


def get_next(input_array, minutes):
    next = []
    for bus in input_array:
        if minutes % bus == 0:
            next.append((minutes // bus) * bus)
        else:
            next.append(((minutes // bus) + 1) * bus)
    return next


def chinese_remainder(n, a):
    """ https://rosettacode.org/wiki/Chinese_remainder_theorem#Python """
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def solve_puzzle_two(input_array):
    remainders = []
    modulos = []
    for idx, value in enumerate(input_array):
        if value == 'x':
            continue
        remainders.append(len(input_array) - (idx + 1))
        modulos.append(int(value))
    print(chinese_remainder(modulos, remainders) - len(input_array) + 1)


def parse_input(data):
    lines = data.splitlines()
    minutes = int(lines[0])
    return minutes, [int(bus) for bus in lines[1].split(',') if bus != 'x']


def parse_input2(data):
    lines = data.splitlines()
    return [bus for bus in lines[1].split(',')]


test_input = """939
7,13,x,x,59,x,31,19
"""

test_input2 = """15
17,x,13,19
"""

test_input3 = """15
67,7,59,61
"""

test_input4 = """15
67,x,7,59,61
"""

test_input5 = """15
67,7,x,59,61
"""
test_input6 = """15
1789,37,47,1889
"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=13)
    input = puzzle.input_data
    if False:
        input = test_input6

    minutes, array = parse_input(input)

    solve_puzzle_one(minutes, array)
    array2 = parse_input2(input)
    solve_puzzle_two(array2)
