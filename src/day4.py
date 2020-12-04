import re

from aocd.models import Puzzle


def solve_puzzle_one(input_array):
    c = 0
    for passport in input_array:
        if 'byr' not in passport:
            continue
        if 'iyr' not in passport:
            continue
        if 'eyr' not in passport:
            continue
        if 'hgt' not in passport:
            continue
        if 'hcl' not in passport:
            continue
        if 'ecl' not in passport:
            continue
        if 'pid' not in passport:
            continue
        c += 1
    print(c)


def solve_puzzle_two(input_array):
    c = 0
    for passport in input_array:
        if 'byr' not in passport or not (
                re.match(r'^\d{4}$', passport['byr']) and 1920 <= int(passport['byr']) <= 2002):
            continue
        if 'iyr' not in passport or not (
                re.match(r'^\d{4}$', passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020):
            continue
        if 'eyr' not in passport or not (
                re.match(r'^\d{4}$', passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030):
            continue
        hgt = re.match(r'^(\d+)(cm|in)$', passport.get('hgt', ''))
        if 'hgt' not in passport or not (hgt
                                         and ((hgt[2] == "cm" and 150 <= int(hgt[1]) <= 193)
                                              or (hgt[2] == "in" and 59 <= int(hgt[1]) <= 76))):
            continue
        if 'hcl' not in passport or not re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
            continue
        if 'ecl' not in passport or not re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']):
            continue
        if 'pid' not in passport or not re.match(r'^\d{9}$', passport['pid']):
            continue
        c += 1
    print(c)


def parse_input(puzzle):
    # array = [parse("")
    #          for line in np.array(puzzle.input_data.splitlines())]
    r = []
    for line in puzzle.input_data.split('\n\n'):
        m = {}
        if not line:
            continue
        for field in line.split():
            m[field.split(":")[0]] = field.split(":")[1]
        r.append(m)

    return r


test_input = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=4)
    array = parse_input(puzzle)
    solve_puzzle_one(array)
    solve_puzzle_two(array)
