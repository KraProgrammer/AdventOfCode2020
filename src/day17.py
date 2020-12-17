import numpy as np
from aocd.models import Puzzle
from funcy import lmap


def solve_puzzle_one(input_array):
    on = {}
    for i, line in enumerate(input_array):
        for j, ch in enumerate(line):
            if ch == '#':
                on[(i, j, 0)] = 1

    size = len(input_array)

    for cycle in range(6):
        size += 2
        new_on = {}
        for x in range(-size, size):
            for y in range(-size, size):
                for z in range(-size, size):
                    neighbours_on = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            for dz in [-1, 0, 1]:
                                if dx == 0 and dy == 0 and dz == 0:
                                    continue
                                if (x + dx, y + dy, z + dz) in on:
                                    neighbours_on += 1
                    if (x, y, z) in on and 2 <= neighbours_on <= 3:
                        new_on[(x, y, z)] = 1
                    elif neighbours_on == 3:
                        new_on[(x, y, z)] = 1
        on = new_on

    print(len(on))


def solve_puzzle_two(input_array):
    on = {}
    for i, line in enumerate(input_array):
        for j, ch in enumerate(line):
            if ch == '#':
                on[(i, j, 0, 0)] = 1

    size = len(input_array)

    for cycle in range(6):
        size += 2
        new_on = {}
        # Possible improvement:
        #   1. build a set that contains all neighbours
        #   2. check rules on all neighbours
        for x in range(-size, size):
            for y in range(-size, size):
                for z1 in range(-size, size):
                    for z2 in range(-size, size):
                        neighbours_on = 0
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                for dz1 in [-1, 0, 1]:
                                    for dz2 in [-1, 0, 1]:
                                        if dx == 0 and dy == 0 and dz1 == 0 and dz2 == 0:
                                            continue
                                        if (x + dx, y + dy, z1 + dz1, z2 + dz2) in on:
                                            neighbours_on += 1
                        if (x, y, z1, z2) in on and 2 <= neighbours_on <= 3:
                            new_on[(x, y, z1, z2)] = 1
                        elif neighbours_on == 3:
                            new_on[(x, y, z1, z2)] = 1
        on = new_on

    print(len(on))


def parse_input(data):
    return np.array(lmap(list, data.splitlines()))


test_input = """.#.
..#
###"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=17)
    if False:
        array = parse_input(test_input)
    else:
        array = parse_input(puzzle.input_data)

    solve_puzzle_one(array)
    solve_puzzle_two(array)
