import numpy as np
from aocd.models import Puzzle
from parse import parse


def solve_puzzle_one(data):
    invalids = []
    invalid_tickets = set()

    for idx, ticket in enumerate(data['n']):
        for value in ticket:
            invalid = True
            for rule in data['r'].items():
                for part in rule[1]:
                    if part[0] <= value <= part[1]:
                        invalid = False
            if invalid:
                invalids.append(value)
                invalid_tickets.add(idx)

    print(sum(invalids))

    return [ticket for idx, ticket in enumerate(data['n']) if idx not in invalid_tickets]


def solve_puzzle_two(data):
    valid_tickets = solve_puzzle_one(data)

    valid_rules_list = np.empty(len(valid_tickets[0]), dtype=list)

    for field_idx in range(len(valid_tickets[0])):
        valid_rules = set()
        for rule in data['r'].items():
            valid = True
            for ticket in valid_tickets:
                if not (rule[1][0][0] <= ticket[field_idx] <= rule[1][0][1]
                        or rule[1][1][0] <= ticket[field_idx] <= rule[1][1][1]):
                    valid = False
            if valid:
                valid_rules.add(rule[0])
        valid_rules_list[field_idx] = valid_rules

    assignments = {}
    while len(assignments) < len(valid_rules_list):
        idx = -1
        rule_name = ''
        for i, assignment in enumerate(valid_rules_list):
            if assignment and len(assignment) == 1:
                idx = i
                rule_name = next(iter(assignment))
                break
        assignments[rule_name] = idx

        for assignment in valid_rules_list:
            if rule_name in assignment:
                assignment.remove(rule_name)

    result = 1
    for rule_name, idx in assignments.items():
        if rule_name.startswith("departure"):
            result *= np.uint64(data['y'][idx])
    print(result)


def parse_input(data):
    blocks = data.split('\n\n')
    rules = {}
    for rule in blocks[0].splitlines():
        result = parse("{field}: {low:d}-{high:d} or {low2:d}-{high2:d}", rule)
        rules[result['field']] = [(result['low'], result['high']), (result['low2'], result['high2'])]

    your = np.fromstring(blocks[1].splitlines()[1], dtype=int, sep=',')
    nearby = [np.fromstring(line, dtype=int, sep=',') for line in blocks[2].splitlines()[1:]]
    return dict(r=rules, y=your, n=nearby)


test_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

test_input2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=16)
    if False:
        array = parse_input(test_input2)
    else:
        array = parse_input(puzzle.input_data)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
