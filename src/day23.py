from aocd.models import Puzzle


class Node:
    def __init__(self, data, prev_node, next_node):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.index = {}

    def append(self, prev, data) -> Node:
        if prev is None:
            node = Node(data, None, None)
            node.next_node = node
            node.prev_node = node
            self.index[data] = node
            return node
        else:
            node = Node(data, prev, prev.next_node)
            prev.next_node = node
            node.next_node.prev_node = node
            self.index[data] = node
            return node

    def get(self, data) -> Node:
        return self.index[data]

    def len(self):
        return len(self.index)

    def to_list(self, start):
        node = self.get(start)
        array = [node.data]
        node = node.next_node
        while node.data != start:
            array.append(node.data)
            node = node.next_node
        return array


def solve_puzzle_one(input):
    print(input)

    llist = LinkedList()
    prev = None
    for num in input:
        prev = llist.append(prev, num)

    current = llist.get(input[0])

    move = 0

    while move < 100:
        move += 1

        pickup_start = current.next_node
        pickup_end = pickup_start.next_node.next_node

        skips = []
        c = pickup_start
        for _ in range(3):
            skips.append(c.data)
            c = c.next_node

        pickup_end.next_node.prev_node = current
        current.next_node = pickup_end.next_node

        num = current.data
        destination = llist.len() if num == 1 else num - 1
        while destination in skips:
            destination = llist.len() if destination == 1 else destination - 1

        destination_node = llist.get(destination)

        pickup_end.next_node = destination_node.next_node
        destination_node.next_node.prev_node = pickup_end

        destination_node.next_node = pickup_start
        pickup_start.prev_node = destination_node

        current = current.next_node

    print(''.join([str(x) for x in llist.to_list(1)[1:]]))


def solve_puzzle_two(input):
    print(input)

    llist = LinkedList()
    prev = None
    for num in input:
        prev = llist.append(prev, num)

    v = llist.len() + 1
    while llist.len() < 1000000:
        prev = llist.append(prev, v)
        v += 1

    current = llist.get(input[0])

    move = 0

    while move < 10000000:
        move += 1

        pickup_start = current.next_node
        pickup_end = pickup_start.next_node.next_node

        skips = []
        c = pickup_start
        for _ in range(3):
            skips.append(c.data)
            c = c.next_node

        pickup_end.next_node.prev_node = current
        current.next_node = pickup_end.next_node

        num = current.data
        destination = llist.len() if num == 1 else num - 1
        while destination in skips:
            destination = llist.len() if destination == 1 else destination - 1

        destination_node = llist.get(destination)

        pickup_end.next_node = destination_node.next_node
        destination_node.next_node.prev_node = pickup_end

        destination_node.next_node = pickup_start
        pickup_start.prev_node = destination_node

        current = current.next_node

    print(llist.get(1).next_node.data)
    print(llist.get(1).next_node.next_node.data)
    print(llist.get(1).next_node.next_node.data * llist.get(1).next_node.data)


def parse_input(data):
    return [int(num) for num in data]


test_input = """389125467"""

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=23)
    input = puzzle.input_data
    if False:
        input = test_input

    solve_puzzle_one(parse_input(input.strip()))
    solve_puzzle_two(parse_input(input.strip()))
