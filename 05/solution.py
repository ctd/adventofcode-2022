#!/usr/bin/env python

from collections import defaultdict
from copy import deepcopy
import re


def parse_puzzle(puzzlein):
    stacksin, instructionsin = puzzlein.split("\n\n")
    return parse_stacks(stacksin), parse_instructions(instructionsin)


def parse_stacks(stacksin):
    stacks = defaultdict(list)
    for line in stacksin.split("\n")[:-1]:
        for i, c in enumerate(line[i] for i in range(1, len(line), 4)):
            if c == " ":
                continue
            stack = i + 1
            stacks[stack].append(c)
    for stack in stacks.values():
        stack.reverse()
    return stacks


def parse_instructions(instructionsin):
    return tuple(
        tuple(int(c) for c in inst)
        for inst in re.findall("move (\d+) from (\d+) to (\d+)", instructionsin)
    )


def execute_instructions(stacksin, instructions, model):
    stacks = deepcopy(stacksin)
    for instruction in instructions:
        moves, a, b = instruction
        if model == 9000:
            for _ in range(int(moves)):
                stacks[b].append(stacks[a].pop())
        elif model == 9001:
            stacks[b] = [*stacks[b], *stacks[a][-moves:]]
            stacks[a] = stacks[a][:-moves]
    return stacks


def solve(puzzle, model):
    stacks = execute_instructions(*puzzle, model)
    answer = ""
    for k, v in sorted(stacks.items()):
        answer += v[-1]
    return answer


def part1(puzzle):
    return solve(puzzle, 9000)


def part2(puzzle):
    return solve(puzzle, 9001)


def tests():
    sample = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
    """

    puzzle = parse_puzzle(sample)
    assert part1(puzzle) == "CMZ"
    assert part2(puzzle) == "MCD"


if __name__ == "__main__":
    tests()
    puzzle = parse_puzzle(open("input").read())
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2: {}".format(part2(puzzle)))
