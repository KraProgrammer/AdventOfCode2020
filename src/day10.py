from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from aocd.models import Puzzle


def solve_puzzle_one(input_array):
    diffs = np.diff(sorted(input_array))
    unique, counts = np.unique(diffs, return_counts=True)
    counts = dict(zip(unique, counts))
    print((counts[1] + 1) * (counts[3] + 1))


def solve_puzzle_two_graph(input_array):
    """
    Networkx impl is to slow
    """
    sort = np.array(sorted(np.append(input_array, 0)))
    graph = nx.DiGraph()
    graph.add_nodes_from(sort)
    for value in sort:
        for jump in [1, 2, 3]:
            if value + jump in sort:
                graph.add_edge(value, value + jump)

    # print_graph(graph)
    count = 0
    for _ in nx.all_simple_paths(graph, 0, sort[-1]):
        count += 1
    print(count)


def solve_puzzle_two_tribonacci(input_array):
    sort = np.array(sorted(input_array))
    counter = defaultdict(int)
    counter[0] = 1
    for value in sort:
        counter[value] = counter[value - 1] + counter[value - 2] + counter[value - 3]

    print(counter[sort[-1]])


def print_graph(graph):
    options = {
        "font_size": 12,
        "node_size": 500,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 1,
    }
    nx.draw_networkx(graph, None, **options)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("off")
    plt.show()


def parse_input(data):
    return np.fromstring(data, dtype=np.int, sep='\n')


test_input = """16
10
15
5
1
11
7
19
6
12
4"""

test_input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=10)
    if False:
        array = parse_input(test_input2)
    else:
        array = parse_input(puzzle.input_data)
    print(array)
    solve_puzzle_one(array)
    solve_puzzle_two_tribonacci(array)
