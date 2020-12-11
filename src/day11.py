from collections import Counter

import numpy as np
from aocd.models import Puzzle
from funcy import lmap


def solve_puzzle_one(input_array):
    input_array = np.pad(input_array, 1, mode='constant')
    input_array, changes = simulate(input_array)
    while changes != 0:
        input_array, changes = simulate(input_array)
    counter = Counter(input_array.flatten())
    print(counter['#'])


def simulate(input_array):
    # print(input_array)
    changes = 0
    result = np.copy(input_array)
    for i in range(1, len(input_array) - 1):
        for j in range(1, len(input_array[0]) - 1):
            neighbours = get_neighbours(input_array, i, j)
            counter = Counter(neighbours)
            if input_array[i, j] == 'L':
                if counter['#'] == 0:
                    result[i, j] = '#'
                    changes += 1
            elif input_array[i, j] == '#':
                if counter['#'] >= 4:
                    result[i, j] = 'L'
                    changes += 1
    return result, changes


def get_neighbours(input_array, i, j):
    neighbours = []
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if k == 0 and l == 0:
                continue
            neighbours.append(input_array[i + k][j + l])
    return neighbours


def solve_puzzle_two(input_array):
    input_array, changes = simulate2(input_array)
    while changes != 0:
        input_array, changes = simulate2(input_array)
    counter = Counter(input_array.flatten())
    print(counter['#'])


def simulate2(input_array):
    # print(input_array)
    changes = 0
    result = np.copy(input_array)
    for i in range(rows):
        for j in range(cols):
            if input_array[i][j] == 'L' and count_occupied(i, j, input_array) == 0:
                result[i][j] = '#'
                changes += 1
            elif input_array[i][j] == '#' and count_occupied(i, j, input_array) >= 5:
                result[i][j] = 'L'
                changes += 1
    return result, changes


def count_occupied(i, j, input_array):
    occupied = 0
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        moved_x = i + x
        moved_y = j + y
        while 0 <= moved_x < rows and 0 <= moved_y < cols:
            if input_array[moved_x][moved_y] != '.':
                occupied += 1 if input_array[moved_x][moved_y] == '#' else 0
                break
            moved_x += x
            moved_y += y
    return occupied


def parse_input(data):
    return np.array(lmap(list, data.splitlines()))


test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=11)
    if False:
        array = parse_input(test_input)
    else:
        array = parse_input(puzzle.input_data)
    print(array)

    rows = len(array)
    cols = len(array[0])

    solve_puzzle_one(array)
    solve_puzzle_two(array)
