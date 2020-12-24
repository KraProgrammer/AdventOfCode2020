from aocd.models import Puzzle


def solve_puzzle_one(input):
    # https://www.redblobgames.com/grids/hexagons/#coordinates
    print(input)
    cube = set()
    for line in input:
        x, y, z = 0, 0, 0
        for direction in line:
            if direction == "e":
                x += 1
                y -= 1
            elif direction == "se":
                y -= 1
                z += 1
            elif direction == "sw":
                x -= 1
                z += 1
            elif direction == "w":
                x -= 1
                y += 1
            elif direction == "nw":
                y += 1
                z -= 1
            elif direction == "ne":
                x += 1
                z -= 1

        if (x, y, z) in cube:
            cube.remove((x, y, z))
        else:
            cube.add((x, y, z))
    print("part1: " + str(len(cube)))
    return cube


def solve_puzzle_two(input):
    cube = solve_puzzle_one(input)

    for _ in range(100):
        relevant = set()
        new_cube = set()
        for (x, y, z) in cube:
            for (dx, dy, dz) in [(0, 0, 0), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
                relevant.add((x + dx, y + dy, z + dz))

        for (x, y, z) in relevant:
            neighbours = 0
            for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
                if (x + dx, y + dy, z + dz) in cube:
                    neighbours += 1
            if (x, y, z) in cube:
                if not (neighbours == 0 or neighbours > 2):
                    new_cube.add((x, y, z))
            elif neighbours == 2:
                new_cube.add((x, y, z))

        cube = new_cube
    print("part2: " + str(len(cube)))


def parse_input(data):
    arr = []
    for line in data.splitlines():
        directions = []
        while line:
            if line.startswith("e"):
                directions.append("e")
                line = line[1:]
            elif line.startswith("se"):
                directions.append("se")
                line = line[2:]
            elif line.startswith("sw"):
                directions.append("sw")
                line = line[2:]
            elif line.startswith("w"):
                directions.append("w")
                line = line[1:]
            elif line.startswith("nw"):
                directions.append("nw")
                line = line[2:]
            elif line.startswith("ne"):
                directions.append("ne")
                line = line[2:]
        arr.append(directions)
    return arr


test_input = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=24)
    input = puzzle.input_data
    if False:
        input = test_input

    # solve_puzzle_one(parse_input(input.strip()))
    solve_puzzle_two(parse_input(input.strip()))
