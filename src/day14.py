from collections import defaultdict
from itertools import product

from aocd.models import Puzzle
from parse import parse


def solve_puzzle_one(data):
    memory = defaultdict(int)

    for line in data.splitlines():
        if line.startswith("mask"):
            mask = parse("mask = {mask}", line)["mask"]
        else:
            inst = parse("mem[{idx:d}] = {value:d}", line)

            value = list(format(inst["value"], '036b'))
            for idx, bit in enumerate(mask):
                if bit == 'X':
                    continue
                else:
                    value[idx] = bit
            memory[inst["idx"]] = int(''.join(value), 2)
    print(sum(memory.values()))


def solve_puzzle_two(data):
    memory = defaultdict(int)

    for line in data.splitlines():
        if line.startswith("mask"):
            mask = parse("mask = {mask}", line)["mask"]
        else:
            inst = parse("mem[{idx:d}] = {value:d}", line)

            value = list(format(inst["idx"], '036b'))
            for idx, bit in enumerate(mask):
                if bit == '0':
                    continue
                else:
                    value[idx] = mask[idx]
            for address in get_addresses(value):
                memory[address] = inst["value"]
    print(sum(memory.values()))


def get_addresses(pattern):
    #  https://stackoverflow.com/questions/52382444/replace-combinations-of-characters
    indices = [i for i, c in enumerate(pattern) if c == 'X']
    for combinations in product('01', repeat=pattern.count('X')):
        for i, c in zip(indices, combinations):
            pattern[i] = c
        yield ''.join(pattern)


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=14)
    solve_puzzle_one(puzzle.input_data)
    solve_puzzle_two(puzzle.input_data)
