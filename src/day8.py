from aocd.models import Puzzle
from parse import parse


def solve_puzzle_one(input_array):
    print(interpret(input_array)[1])


def solve_puzzle_two(input_array):
    for i in range(len(input_array)):
        if input_array[i] is None:
            continue
        if input_array[i]['operation'] == 'acc':
            continue
        updated_input = input_array.copy()
        if input_array[i]['operation'] == 'jmp':
            updated_input[i] = {'operation': 'nop', 'argument': input_array[i]['argument']}
            if interpret(updated_input)[0]:
                print(interpret(updated_input)[1])
        if input_array[i]['operation'] == 'nop':
            updated_input[i] = {'operation': 'jmp', 'argument': input_array[i]['argument']}
            if interpret(updated_input)[0]:
                print(interpret(updated_input)[1])


def interpret(input_array):
    s = set()
    acc = 0
    i = 0
    while i < len(input_array):
        if i in s:
            return False, acc
        s.add(i)
        if input_array[i] is None:
            return acc
        if input_array[i]['operation'] == 'nop':
            i = i + 1
            continue
        if input_array[i]['operation'] == 'acc':
            acc += input_array[i]['argument']
            i = i + 1
            continue
        if input_array[i]['operation'] == 'jmp':
            i += input_array[i]['argument']
            continue
        else:
            print("Wrong instruction")
    return True, acc


def parse_input(data):
    return [parse("{operation:w} {argument:d}", line)
            for line in data.split("\n")]


test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=8)
    if False:
        array = parse_input(test_input)
    else:
        array = parse_input(puzzle.input_data)
    print(array)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
