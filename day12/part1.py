import re

NORTH, EAST, SOUTH, WEST = (0, 1), (1, 0), (0, -1), (-1, 0)


def add(p1, p2, n):
    return p1[0] + n * p2[0], p1[1] + n * p2[1]


def turn_right(vector, times):
    for i in range(times):
        vector = (vector[1], -vector[0])
    return vector


def solve(instructions):
    pos = (0, 0)
    facing = EAST
    for (letter, val) in instructions:
        if letter == 'F':
            pos = add(pos, facing, val)
        if letter == 'N':
            pos = add(pos, NORTH, val)
        if letter == 'S':
            pos = add(pos, SOUTH, val)
        if letter == 'W':
            pos = add(pos, WEST, val)
        if letter == 'E':
            pos = add(pos, EAST, val)
        if letter == 'R':
            facing = turn_right(facing, val // 90)
        if letter == 'L':
            facing = turn_right(facing, 4 - val // 90)
    return abs(pos[0]) + abs(pos[1])


def parse(file_name):
    instructions = []
    possibles = set()
    with open(file_name, 'r') as f:
        for line in f.readlines():
            letter, val = re.match(r'([SNEWLRF])(\d+)$', line.strip()).groups()
            if letter in 'LR':
                possibles.add(val)
            instructions.append((letter, int(val)))
    return instructions


if __name__ == "__main__":
    print(solve(parse("data.txt")))
