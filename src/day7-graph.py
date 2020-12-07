import re

import networkx as nx
import numpy as np
from aocd.models import Puzzle

pattern = re.compile(r'((\d)?\s?(\w*\s\w+)\s(bags?))')


def solve_puzzle_one(graph):
    print(len(nx.ancestors(graph, 'shiny gold')))


def solve_puzzle_two(graph):
    print(count_bags(graph, 'shiny gold'))


def count_bags(graph, node):
    sum = 0
    for successor in graph.successors(node):
        weight = graph[node][successor]['weight']
        sum += count_bags(graph, successor) * weight + weight
    return sum


def parse_input(data):
    g = nx.DiGraph()
    for rule in np.array(data.splitlines()):
        matches = pattern.findall(rule)
        for i in range(1, len(matches)):
            g.add_edge(matches[0][2], matches[i][2], weight=int(matches[i][1]) if matches[i][1] else 0)
    return g


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
        graph = parse_input(test_input)
    else:
        graph = parse_input(puzzle.input_data)
    # print(array)
    solve_puzzle_one(graph)
    solve_puzzle_two(graph)
