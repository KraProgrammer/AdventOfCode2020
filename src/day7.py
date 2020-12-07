import re
from collections import defaultdict

import numpy as np
from aocd.models import Puzzle

pattern = re.compile(r'(?P<c>(\w*\s\w+)\s(bags?))')
pattern2 = re.compile(r'((\d)?\s?(\w*\s\w+)\s(bags?))')


def solve_puzzle_one(input_array):
    d = create_dict(input_array)
    # print([item for sublist in d.values() for item in sublist])
    result = [find_gold(d, key) for key in d.keys()]
    print(sum(result))


def find_gold(d, color):
    if len(d.get(color, [])) == 0:
        return False
    if 'shiny gold' in d.get(color):
        return True
    else:
        return any([find_gold(d, subColor) for subColor in d[color]])


def create_dict(input_array):
    d = defaultdict(list)
    for rule in input_array:
        matches = pattern.findall(rule)
        if matches[1][0] == 'no other bags':
            continue
        for i in range(1, len(matches)):
            d[matches[0][1]].append(matches[i][1])
    return d


def solve_puzzle_two(input_array):
    d = create_dict2(input_array)
    print(d)
    print(count_bags_for(d, 'shiny gold'))


def create_dict2(input_array):
    d = defaultdict(list)
    for rule in input_array:
        matches = pattern2.findall(rule)
        if matches[1][0] == ' no other bags':
            continue
        for i in range(1, len(matches)):
            d[matches[0][2]].append((matches[i][2], matches[i][1]))
    return d


def count_bags_for(d, color):
    if len(d.get(color, [])) == 0:
        return 0
    sum = 0
    for subColor in d[color]:
        sum += count_bags_for(d, subColor[0]) * int(subColor[1]) + int(subColor[1])
    return sum


def parse_input(data):
    return np.array(data.splitlines())


test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
faded blue bags contain no other bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
dotted black bags contain no other bags.
"""

test_input2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=7)
    if False:
        array = parse_input(test_input)
    else:
        array = parse_input(puzzle.input_data)
    # print(array)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
