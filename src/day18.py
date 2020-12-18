from aocd.models import Puzzle
from lark import Lark, Transformer, v_args

calc_grammar = """
    ?start: mulsum
    ?mulsum: atom
        | mulsum "+" atom   -> add
        | mulsum "-" atom   -> sub
        | mulsum "*" atom  -> mul
        | mulsum "/" atom  -> div
    ?atom: NUMBER           -> number
         | NAME             -> var
         | "(" mulsum ")"
    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

calc_grammar2 = """
    ?start: product
    ?product: sum
        | sum "*" product  -> mul
        | sum "/" product  -> div
    ?sum: atom
        | sum "+" atom   -> add
        | sum "-" atom   -> sub
    ?atom: NUMBER           -> number
         | "(" product ")"
    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""


@v_args(inline=True)  # Affects the signatures of the methods
class CalculateTree(Transformer):
    """
    Taken from https://github.com/lark-parser/lark/blob/master/examples/calc.py
    """
    number = float

    def __init__(self):
        super().__init__()
        self.vars = {}

    def add(self, mulsum, atom):
        return mulsum + atom

    def sub(self, mulsum, atom):
        return mulsum - atom

    def mul(self, mulsum, atom):
        return mulsum * atom

    def div(self, mulsum, atom):
        return mulsum / atom


def solve_puzzle_one(input_array):
    calc_parser = Lark(calc_grammar, parser='lalr', transformer=CalculateTree())
    calc = calc_parser.parse

    print(sum([calc(line) for line in input_array]))


def solve_puzzle_two(input_array):
    calc_parser = Lark(calc_grammar2, parser='lalr', transformer=CalculateTree())
    calc = calc_parser.parse

    print(sum([calc(line) for line in input_array]))


def parse_input(data):
    return data.splitlines()


test_input = """1 + 2 * 3 + 4 * 5 + 6
"""

test_input2 = """1 + (2 * 3) + (4 * (5 + 6))
"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=18)
    input = puzzle.input_data
    if False:
        input = test_input2

    solve_puzzle_one(parse_input(input.strip()))
    solve_puzzle_two(parse_input(input.strip()))
