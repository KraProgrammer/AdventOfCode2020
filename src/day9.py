import numpy as np
from aocd.models import Puzzle

number_count = 25


def solve_puzzle_one(input_array):
    for i in range(number_count, len(input_array)):
        if find_wrong_number(input_array, i):
            print(input_array[i])
            return input_array[i]
    print('Not found')


def find_wrong_number(input_array, curr):
    for j in range(curr - number_count, curr):
        for k in range(curr - number_count, curr):
            if input_array[j] != input_array[k] and input_array[j] + input_array[k] == input_array[curr]:
                return False
    return True


def solve_puzzle_two(input_array):
    number = solve_puzzle_one(input_array)

    for i in range(len(input_array)):
        for j in range(i + 1, len(input_array)):
            curr_sum = sum(input_array[i:j])
            if curr_sum == number:
                print(min(input_array[i:j]) + max(input_array[i:j]))
                return
            if curr_sum > number:
                break


def parse_input(data):
    return np.fromstring(data, dtype=np.int64, sep='\n')


test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=9)
    if False:
        array = parse_input(test_input)
    else:
        array = parse_input(puzzle.input_data)
    print(array)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
