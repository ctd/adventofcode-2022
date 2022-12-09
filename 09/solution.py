#!/usr/bin/env python

import re

DIRECTIONS = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}


def parse_puzzle(puzzlein):
    return tuple((d, int(i)) for d, i in re.findall("([UDLR]) (\d+)", puzzlein))


def execute(puzzle, number_of_knots=2):
    start = (0, 0)
    knots = [[start] for _ in range(number_of_knots)]
    head = knots[0]
    for direction, iterations in puzzle:
        for _ in range(iterations):
            cur_y, cur_x = head[-1]
            dif_y, dif_x = DIRECTIONS[direction]
            head.append((cur_y + dif_y, cur_x + dif_x))
            for i, tail in enumerate(knots[1:], start=1):
                tail.append(tail_follow(knots[i - 1][-1], tail[-1]))
    return knots


def max_move(i):
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return i


def tail_follow(head, tail):
    head_y, head_x = head
    tail_y, tail_x = tail
    diff_y = head_y - tail_y
    diff_x = head_x - tail_x
    if abs(diff_y) <= 1 and abs(diff_x) <= 1:
        return tail
    new_y = tail_y + max_move(diff_y)
    new_x = tail_x + max_move(diff_x)
    return new_y, new_x


def part1(puzzle):
    return len(set(execute(puzzle, number_of_knots=2)[-1]))


def part2(puzzle):
    return len(set(execute(puzzle, number_of_knots=10)[-1]))


def tests():
    sample1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
    sample2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
    puzzle = parse_puzzle(sample1)
    assert part1(puzzle) == 13
    assert part2(puzzle) == 1
    puzzle = parse_puzzle(sample2)
    assert part2(puzzle) == 36


if __name__ == "__main__":
    tests()
    puzzle = parse_puzzle(open("input").read())
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2: {}".format(part2(puzzle)))
