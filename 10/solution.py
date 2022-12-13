#!/usr/bin/env python

import re


def parse_puzzle(puzzlein):
    return tuple(re.findall("(noop|addx) ?([-\d]+)?", puzzlein))


def tests():
    sample = (("noop", ""), ("addx", "3"), ("addx", "-5"))
    cycles = execute(sample)
    assert cycles == [1, 1, 1, 1, 4, 4, -1]
    sample = parse_puzzle(open("sample").read())
    assert part1(sample) == 13140


def execute(puzzle):
    x = 1
    cycles = [x]
    for instruction, param in puzzle:
        cycles.append(x)
        if instruction == "addx":
            cycles.append(x)
            x += int(param)
    cycles.append(x)
    return cycles


def draw(cycles, height=6, width=40):
    i = 1
    for y in range(height):
        for x in range(width):
            x_val = cycles[i]
            if x in range(x_val - 1, x_val + 2):
                print("#", end="")
            else:
                print(".", end="")
            i += 1
        print()


def part1(puzzle):
    cycles = execute(puzzle)
    return sum((cycles[i] * i for i in (20, 60, 100, 140, 180, 220,)))


def part2(puzzle):
    draw(execute(puzzle))


if __name__ == "__main__":
    tests()
    puzzle = parse_puzzle(open("input").read())
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2:")
    part2(puzzle)
