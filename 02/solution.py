#!/usr/bin/env python

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

SHOULD_LOSE = "X"
SHOULD_DRAW = "Y"
SHOULD_WIN = "Z"

WINS = ((ROCK, PAPER), (PAPER, SCISSORS), (SCISSORS, ROCK))
LOSES = ((ROCK, SCISSORS), (PAPER, ROCK), (SCISSORS, PAPER))


def normalise_move(c):
    if type(c) == int:
        return c
    i = ord(c)
    if i >= ord("X"):
        i -= ord("X")
    else:
        i -= ord("A")
    return 1 + i


def find_move(moveset, opponent):
    return next((m[1] for m in moveset if m[0] == normalise_move(opponent)))


def score(opponent, mine):
    oppo_i = normalise_move(opponent)
    mine_i = normalise_move(mine)
    if oppo_i == mine_i:
        return DRAW + mine_i
    scenario = (oppo_i, mine_i)
    if scenario in WINS:
        return WIN + mine_i
    if scenario in LOSES:
        return LOSE + mine_i


def play_p2_strat(opponent, strat):
    if strat == SHOULD_DRAW:
        mine = opponent
    else:
        if strat == SHOULD_WIN:
            moveset = WINS
        elif strat == SHOULD_LOSE:
            moveset = LOSES
        mine = find_move(moveset, opponent)
    return score(opponent, mine)


def part1(strategy):
    return sum((score(*game) for game in strategy))


def part2(strategy):
    return sum((play_p2_strat(*game) for game in strategy))


def tests():
    sample = [["A", "Y"], ["B", "X"], ["C", "Z"]]
    assert part1(sample) == 15
    assert part2(sample) == 12


if __name__ == "__main__":
    strategy = [x.strip().split(" ") for x in open("input").readlines()]
    tests()
    print("Part 1: {}".format(part1(strategy)))
    print("Part 2: {}".format(part2(strategy)))
