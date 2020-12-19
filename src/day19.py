from aocd.models import Puzzle


def solve_puzzle_one(input_tuple):
    count = 0
    for message in input_tuple[1]:
        matched, start = match_rule(input_tuple[0], '0', message, 0)
        if matched and len(message) == start:
            count += 1

    print(count)


def match_rule(rules, curr_rule, curr_str, start):
    match = False
    for alt in rules[curr_rule]:
        if alt[0][0].isdigit():
            sub_rule_match = True
            curr_start = start
            for i, sub_rule in enumerate(alt):
                matched, start = match_rule(rules, sub_rule, curr_str, start)
                if not matched:
                    sub_rule_match = False
                    start = curr_start
                    break
            if sub_rule_match:
                match = True
                break
        else:
            if curr_str[start] == alt[0][1]:
                return True, start + 1
            else:
                return False, 0
    return match, start


def match_using_stack(curr_str, stack):
    if len(stack) > len(curr_str):
        return False
    elif len(stack) == 0 or len(curr_str) == 0:
        return len(stack) == len(curr_str)
    c = stack.pop()
    if not c.isdigit():
        if curr_str[0] == c[1]:
            return match_using_stack(curr_str[1:], stack.copy())
    else:
        for rule in rules[c]:
            if match_using_stack(curr_str, stack + list(reversed(rule))):
                return True
    return False


def solve_puzzle_two(input_tuple):
    count = 0
    for message in input_tuple[1]:
        if match_using_stack(message, list(reversed(rules['0'][0]))):
            count += 1
    print(count)


def parse_input(data):
    rules = {}
    for rule in data.split("\n\n")[0].splitlines():
        rules[rule.split(":")[0].strip()] = [alt.strip().split(' ') for alt in rule.split(":")[1].strip().split('|')]

    return rules, data.split("\n\n")[1].splitlines()


test_input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

test_input2 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=19)
    input = puzzle.input_data
    if False:
        input = test_input2

    solve_puzzle_one(parse_input(input.strip()))
    rules, messages = parse_input(input.strip())
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    solve_puzzle_two((rules, messages))
