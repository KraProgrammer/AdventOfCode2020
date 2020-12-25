from aocd.models import Puzzle


def solve_puzzle_one(input):
    cpk = input[0]
    dpk = input[1]
    print(cpk)
    print(dpk)

    pks = calc_pks()
    cpk_ls = pks[cpk]
    dpk_ls = pks[dpk]
    assert transform(cpk_ls, dpk) == transform(dpk_ls, cpk)
    print(transform(dpk_ls, cpk))


def transform(lz, sn):
    v = 1
    for _ in range(lz):
        v = v * sn
        v = v % 20201227
    return v


def calc_pks(sn=7):
    d = {}
    v = 1
    for i in range(1, 20000000):
        v = v * sn
        v = v % 20201227
        d[v] = i
    return d


def parse_input(data):
    return int(data.splitlines()[0]), int(data.splitlines()[1])


test_input = """5764801
17807724"""

# parse single line:        data.splitlines() ||  np.array(data.splitlines())
# parse integer:            np.fromstring(puzzle.input_data, dtype=int, sep='\n')
# parse with regex:         [parse("{low:d}-{high:d} {char:l}: {pass:w}", line) for line in data.split("\n")]
# parse string as chars:    np.array(lmap(list, data.split("\n")), dtype=object)
# parse and store to dict:  [dict([pp.split(":") for pp in re.split(r"\s", line)]) for line in data.split("\n\n")]
# parse and store to set:   [lmap(set, group.split("\n")) for group in data.split("\n\n")]


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=25)
    input = puzzle.input_data
    if False:
        input = test_input

    solve_puzzle_one(parse_input(input.strip()))
