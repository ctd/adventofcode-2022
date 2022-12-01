#!/usr/bin/env python


def parse_elves(puzzle_input):
    elves = list()
    for elf in puzzle_input.split("\n\n"):
        elves.append([int(food) for food in elf.split("\n") if food])
    return sorted(elves)


def part1(elves):
    return [sum(elf) for elf in elves][-1]


def part2(elves):
    return sum([sum(elf) for elf in elves][-3:])


if __name__ == "__main__":
    elves = parse_elves(open("input", "r").read())
    print("Part 1: {}".format(part1(elves)))
    print("Part 2: {}".format(part2(elves)))
