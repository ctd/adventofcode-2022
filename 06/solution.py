#!/usr/bin/env python


def tests():
    p1_samples = {
        "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
        "nppdvjthqldpwncqszvftbrmjlhg": 6,
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11,
    }
    for k, v in p1_samples.items():
        assert part1(k) == v

    p2_samples = {
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
        "bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
        "nppdvjthqldpwncqszvftbrmjlhg": 23,
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26,
    }
    for k, v in p2_samples.items():
        assert part2(k) == v


def all_elements_unique(chars):
    return len(chars) == len(set(chars))


def find_marker(puzzle, num_chars):
    for i in range(num_chars, len(puzzle)):
        if all_elements_unique(puzzle[i - num_chars : i]):
            return i


def part1(puzzle):
    return find_marker(puzzle, 4)


def part2(puzzle):
    return find_marker(puzzle, 14)


if __name__ == "__main__":
    tests()
    puzzle = open("input").read().strip()
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2: {}".format(part2(puzzle)))
