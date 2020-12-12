from day12.part1 import parse, add, turn_right, NORTH, EAST, SOUTH, WEST


def solve(instructions):
    pos = (0, 0)
    waypoint = (10, 1)
    for (letter, val) in instructions:
        if letter == 'F':
            pos = add(pos, waypoint, val)
        if letter == 'N':
            waypoint = add(waypoint, NORTH, val)
        if letter == 'S':
            waypoint = add(waypoint, SOUTH, val)
        if letter == 'W':
            waypoint = add(waypoint, WEST, val)
        if letter == 'E':
            waypoint = add(waypoint, EAST, val)
        if letter == 'R':
            waypoint = turn_right(waypoint, val // 90)
        if letter == 'L':
            waypoint = turn_right(waypoint, 4 - val // 90)
    return abs(pos[0]) + abs(pos[1])


if __name__ == "__main__":
    print(solve(parse("data.txt")))
