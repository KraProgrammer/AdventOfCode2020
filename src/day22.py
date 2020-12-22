from collections import deque

from aocd.models import Puzzle


def solve_puzzle_one(decks):
    print(decks[0])
    print(decks[1])

    while len(decks[0]) > 0 and len(decks[1]) > 0:
        c1 = decks[0].popleft()
        c2 = decks[1].popleft()
        if c1 > c2:
            decks[0].append(c1)
            decks[0].append(c2)
        else:
            decks[1].append(c2)
            decks[1].append(c1)

    if decks[0]:
        calc_score(decks[0])
    else:
        calc_score(decks[1])


def calc_score(queue):
    score = 0
    for i, c in enumerate(queue):
        score += (len(queue) - i) * c
    print(score)


def solve_puzzle_two(decks):
    print(decks[0])
    print(decks[1])
    _, winner = play_game(decks[0], decks[1])
    calc_score(winner)


def play_game(deck1, deck2):
    seen = set()
    while len(deck1) > 0 and len(deck2) > 0:
        r_state = (tuple(deck1), tuple(deck2))
        if r_state in seen:
            return True, deck1
        seen.add(r_state)

        c1 = deck1.popleft()
        c2 = deck2.popleft()

        if len(deck1) >= c1 and len(deck2) >= c2:
            new_deck1 = deque([deck1[x] for x in range(c1)])
            new_deck2 = deque([deck2[x] for x in range(c2)])
            p1_wins, _ = play_game(new_deck1, new_deck2)
        else:
            p1_wins = c1 > c2

        if p1_wins:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)

    if deck1:
        return True, deck1
    else:
        return False, deck2


def parse_input(data):
    deck1 = deque()
    deck2 = deque()
    for card in data.split("\n\n")[0].splitlines()[1:]:
        deck1.append(int(card))
    for card in data.split("\n\n")[1].splitlines()[1:]:
        deck2.append(int(card))
    return deck1, deck2


test_input = """Player 1:
43
19

Player 2:
2
29
14"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=22)
    input = puzzle.input_data
    if False:
        input = test_input

    solve_puzzle_one(parse_input(input.strip()))
    solve_puzzle_two(parse_input(input.strip()))
