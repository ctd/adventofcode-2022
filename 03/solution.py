#!/usr/bin/env python

from functools import reduce


def priority(char):
    base = 1 if char.islower() else 27
    pos = ord(char.lower()) - ord("a")
    return base + pos


def needs_rearrange(line):
    half = int(len(line) / 2)
    first = set(line[:half])
    second = set(line[half:])
    return common((first, second))


def common(items):
    return reduce(lambda a, b: a.intersection(b), map(set, items))


def part1(puzzle):
    return sum(priority(c) for line in puzzle for c in needs_rearrange(line))


def part2(puzzle):
    return sum(
        priority(c)
        for lines in (puzzle[x : x + 3] for x in range(0, len(puzzle), 3))
        for c in common(lines)
    )


def tests():
    sample = (
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    )
    assert part1(sample) == 157
    assert part2(sample) == 70


if __name__ == "__main__":
    tests()
    puzzle = tuple(l.strip() for l in open("input").readlines())
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2: {}".format(part2(puzzle)))
