#!/usr/bin/env python

import re


def parse_puzzle(lines):
    pairs = list()
    for line in lines:
        pair = list()
        for match in re.findall("(\d+)-(\d+)", line):
            pair.append(set(range(int(match[0]), int(match[1]) + 1)))
        pairs.append(pair)
    return pairs


def pair_overlaps(pair):
    a, b = pair
    return a.issubset(b) or a.issuperset(b)


def pair_intersects(pair):
    a, b = pair
    return len(a.intersection(b)) > 0


def tests():
    sample = (
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    )
    puzzle = parse_puzzle(sample)
    assert part1(puzzle) == 2
    assert part2(puzzle) == 4


def part1(puzzle):
    return sum(map(pair_overlaps, puzzle))


def part2(puzzle):
    return sum(map(pair_intersects, puzzle))


if __name__ == "__main__":
    tests()
    puzzle = parse_puzzle(open("input").readlines())
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2: {}".format(part2(puzzle)))
