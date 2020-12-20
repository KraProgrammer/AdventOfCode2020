from dataclasses import dataclass
from functools import reduce

import numpy as np
from aocd.models import Puzzle
from funcy import lmap


@dataclass
class Tile:
    id: int
    borders: list
    body: np.ndarray
    matching_borders = []
    used = 0


@dataclass
class Update:
    rot = 0
    flip = False


def solve_puzzle_one(tiles):
    borders = []
    for tile in tiles:
        borders.extend(tile.borders)

    corners = []
    for tile in tiles:
        matching_borders = []
        for border in tile.borders:
            if borders.count(border) >= 2:
                matching_borders.append(border)
        tile.used = len(matching_borders)
        tile.matching_borders = matching_borders
        if tile.used == 4:
            corners.append(int(tile.id))

    print(corners)
    assert len(corners) == 4
    print('part 1:', reduce(lambda x, y: x * y, corners))
    return tiles, corners


pattern = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()


def flip(array):
    return np.flip(array, axis=0)


def rotate(array):
    return np.rot90(array)


def solve_puzzle_two(tiles):
    tiles, corners = solve_puzzle_one(tiles)

    tile_map = {tile.id: tile for tile in tiles}

    len_grid = int(np.sqrt(len(tiles)))

    grid = np.array([None] * len(tiles)).reshape(len_grid, len_grid)
    grid[0][0] = tile_map[str(corners[0])]
    del tile_map[str(corners[0])]

    last_hash = grid[0][0].matching_borders[0]

    for i in range(1, len_grid):
        grid[i][0] = find_next_tile_border(tile_map, last_hash)
        last_hash = get_last_hash(grid[i][0], last_hash)
        del tile_map[str(grid[i][0].id)]

    last_hash = grid[0][0].matching_borders[1]

    for i in range(1, len_grid):
        grid[0][i] = find_next_tile_border(tile_map, last_hash)
        last_hash = get_last_hash(grid[0][i], last_hash)
        del tile_map[str(grid[0][i].id)]

    for i in range(1, len_grid):
        for j in range(1, len_grid):
            grid[i][j] = find_next_tile(tile_map, grid[i - 1][j], grid[i][j - 1])
            del tile_map[str(grid[i][j].id)]

    array = rotate(rotate(np.array(grid[0][0].body)))  # manuel brute forced
    # array = flip(np.array(grid[0][0].body)) # for test case

    last = array
    first = [last]

    for i in range(1, len_grid):
        last = find_array(grid[0][i].body, last[:, -1])
        first.append(last)

    big_grid = []
    for col in range(len_grid):
        last = first[col]
        big_col = remove_border(last)
        for row in range(1, len_grid):
            last = find_array2(grid[row][col].body, last[-1, :])
            big_col = np.append(big_col, remove_border(last), axis=0)

        if col == 0:
            big_grid = big_col
        else:
            big_grid = np.append(big_grid, big_col, axis=1)

    print("part 2: " + str(count_monsters(big_grid)))


def is_monster(v, di, dj):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if pattern[i][j] == "#" and v[i + di][j + dj] != "#":
                return False
    return True


def count_monsters(big_grid):
    for i in range(2):
        for j in range(4):
            cnt = 0
            for di in range(0, len(big_grid) - len(pattern)):
                for dj in range(0, len(big_grid) - len(pattern[0])):
                    if is_monster(big_grid, di, dj):
                        cnt += 1
            if cnt > 0:
                unique, counts = np.unique(big_grid, return_counts=True)
                c = dict(zip(unique, counts))
                return c["#"] - "".join(pattern).count("#") * cnt
            big_grid = rotate(big_grid)
        big_grid = flip(big_grid)


def remove_border(array):
    return array[1:len(array[0]) - 1, 1:len(array[0]) - 1]


def find_array(curr, last):
    for f in range(2):
        for r in range(4):
            b = curr
            if f:
                b = flip(b)
            for rot in range(r):
                b = rotate(b)
            if tuple(b[:, 0]) == tuple(last):
                return b

    assert False


def find_array2(curr, last):
    for f in range(2):
        for r in range(4):
            b = curr
            if f:
                b = flip(b)
            for rot in range(r):
                b = rotate(b)
            if tuple(b[0, :]) == tuple(last):
                return b

    assert False


def find_next_tile(tile_map, left, upper):
    for (id, tile) in tile_map.items():
        if len(set(tile.borders).intersection(set(left.borders))) == 2 \
                and len(set(tile.borders).intersection(set(upper.borders))) == 2:
            return tile
    assert False


def get_last_hash(tile, curr_last):
    curr_idx = tile.borders.index(curr_last)
    new_idx = (curr_idx + 2) % 4
    if curr_idx >= 4:
        new_idx += 4

    return tile.borders[new_idx]


def find_next_tile_border(tile_map, last_hash):
    for (id, tile) in tile_map.items():
        if last_hash in tile.borders:
            return tile


def parse_input(data):
    tiles = []
    for tile in data.split("\n\n"):
        top = tile.splitlines()[0]
        body = tile.splitlines()[1:]
        grid = np.array(lmap(list, body))

        id = top.split(" ")[1][:-1]

        tiles.append(Tile(id, get_borders(grid), grid))
    return tiles


def get_borders(grid):
    borders = [hash(tuple((grid[0, :]))),
               hash(tuple((grid[:, 0]))),
               hash(tuple((grid[-1, :]))),
               hash(tuple((grid[:, -1]))),
               hash(tuple((reversed(grid[0, :])))),
               hash(tuple((reversed(grid[:, 0])))),
               hash(tuple((reversed(grid[-1, :])))),
               hash(tuple((reversed(grid[:, -1]))))]

    return borders


test_input = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=20)
    input = puzzle.input_data
    if False:
        input = test_input

    # solve_puzzle_one(parse_input(input.strip()))
    solve_puzzle_two(parse_input(input.strip()))
