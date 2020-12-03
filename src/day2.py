from aocd.models import Puzzle


def solve_puzzle_one(input_array):
    count = 0
    for line in input_array:
        partition = line.rpartition(':')
        pattern = partition[0].rpartition(' ')
        range = pattern[0]
        char = pattern[2]
        start = int(range.split('-')[0])
        end = int(range.split('-')[1])
        nums = partition[2].count(char)
        if start <= nums <= end:
            count += 1
    print(count)


def solve_puzzle_two(input_array):
    count = 0
    for line in input_array:
        partition = line.rpartition(':')
        pattern = partition[0].rpartition(' ')
        range = pattern[0]
        char = pattern[2]
        first = int(range.split('-')[0])
        second = int(range.split('-')[1])
        if sum([partition[2][first] == char, partition[2][second] == char]) == 1:
            count += 1
    print(count)


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=2)
    array = puzzle.input_data.splitlines()
    print(array)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
