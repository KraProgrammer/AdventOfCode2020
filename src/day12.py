import math

from aocd.models import Puzzle
from parse import parse


def solve_puzzle_one(input_array):
    direction = ['N', 'E', 'S', 'W']
    x, y = 0, 0
    d = 90
    for move in input_array:
        if move['direction'] == 'L':
            d = (d - move['steps'] + 360) % 360
        elif move['direction'] == 'R':
            d = (d + move['steps'] + 360) % 360
        elif move['direction'] == 'F':
            x, y = do_move(direction[d // 90], move['steps'], x, y)
        else:
            x, y = do_move(move['direction'], move['steps'], x, y)
    print(abs(x) + abs(y))


def do_move(direction, steps, x, y):
    if direction == 'N':
        y -= steps
    elif direction == 'S':
        y += steps
    elif direction == 'E':
        x += steps
    elif direction == 'W':
        x -= steps
    return x, y


def solve_puzzle_two(input_array):
    x_ship, y_ship = 0, 0
    x_point, y_point = 10, -1
    for move in input_array:
        if move['direction'] == 'L':
            x_point, y_point = calc_point(x_point, y_point, 360 - move['steps'])
        elif move['direction'] == 'R':
            x_point, y_point = calc_point(x_point, y_point, move['steps'])
        elif move['direction'] == 'F':
            x_ship += x_point * move['steps']
            y_ship += y_point * move['steps']
        else:
            x_point, y_point = do_move(move['direction'], move['steps'], x_point, y_point)
    print(abs(x_ship) + abs(y_ship))


def calc_point(x, y, angle):
    # https://math.stackexchange.com/questions/1267644/move-a-point-with-known-angle-on-a-circle
    angle = math.radians(angle)
    x_new = math.cos(angle) * x - math.sin(angle) * y
    y_new = math.sin(angle) * x + math.cos(angle) * y
    return round(x_new), round(y_new)


def parse_input(data):
    return [parse("{direction:l}{steps:d}", line) for line in data.splitlines()]


test_input = """F10
N3
F7
R90
F11
"""

test_input2 = """F10
N3
F7
L90
F11
"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=12)
    if False:
        array = parse_input(test_input2)
    else:
        array = parse_input(puzzle.input_data)
    print(array)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
