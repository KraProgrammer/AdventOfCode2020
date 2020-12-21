from collections import defaultdict

from aocd.models import Puzzle


def solve_puzzle_one(input_array):
    counter, ingredients, allergens, possible_allergens = get_data(input_array)

    c = 0
    for i in ingredients:
        if not possible_allergens[i]:
            c += counter[i]
    print(c)


def get_data(input_array):
    ingredients = set()
    allergens = set()
    for i, a in input_array:
        ingredients = ingredients.union(i)
        allergens = allergens.union(a)
    possible_allergens = {i: allergens.copy() for i in ingredients}
    counter = defaultdict(int)
    for i_of_food, a_of_food in input_array:
        for a in a_of_food:
            for i in ingredients:
                if i not in i_of_food:
                    possible_allergens[i].discard(a)

        for i in i_of_food:
            counter[i] += 1
    return counter, ingredients, allergens, possible_allergens


def solve_puzzle_two(input_array):
    counter, ingredients, allergens, possible_allergens = get_data(input_array)

    mapping = {}
    used = set()
    while len(mapping) < len(allergens):
        for i in ingredients:
            possible = [a for a in possible_allergens[i] if a not in used]
            if len(possible) == 1:
                mapping[i] = possible[0]
                used.add(possible[0])

    s = ""
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    array = [k for k, v in sorted(mapping.items(), key=lambda item: item[1])]

    print(','.join(array))


def parse_input(data):
    array = []
    for line in data.splitlines():
        i, rest = line.split('(contains ')
        ingredients = set(i.split())
        allergens = set(rest[:-1].split(", "))
        array.append((ingredients, allergens))

    return array


test_input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=21)
    input = puzzle.input_data
    if False:
        input = test_input

    solve_puzzle_one(parse_input(input.strip()))
    solve_puzzle_two(parse_input(input.strip()))
