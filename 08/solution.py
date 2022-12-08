#!/usr/bin/env python


def parse_puzzle(puzzlein):
    return tuple(tuple(int(x) for x in y) for y in puzzlein)


def adjacent(grid, y, x):
    max_y, max_x = len(grid), len(grid[y])
    return (
            ((i, x) for i in range(y - 1, -1, -1)),
            ((i, x) for i in range(y + 1, max_y)),
            ((y, i) for i in range(x - 1, -1, -1)),
            ((y, i) for i in range(x + 1, max_x)),
        )


def is_visible(grid, y, x):
    edge_y, edge_x = (0, len(grid) - 1), (0, len(grid[y]) - 1)
    height = grid[y][x]

    return (
        y in edge_y
        or x in edge_x
        or any(
            max(grid[j][k] for j, k in direction) < height
            for direction in adjacent(grid, y, x)
        )
    )


def scenic_score(grid, y, x):
    edge_y, edge_x = (0, len(grid) - 1), (0, len(grid[0]) - 1)
    height = grid[y][x]

    score = 1
    for direction in adjacent(grid, y, x):
        for i, coord in enumerate(direction):
            j, k = coord
            if grid[j][k] >= height or j in edge_y or k in edge_x:
                score *= i + 1
                break

    return score


def part1(grid):
    return sum(
        is_visible(grid, y_pos, x_pos)
        for y_pos, y in enumerate(grid)
        for x_pos, _ in enumerate(y)
    )


def part2(grid):
    return max(
        scenic_score(grid, y_pos, x_pos)
        for y_pos, y in enumerate(grid)
        for x_pos, _ in enumerate(y)
    )


def tests():
    sample = (
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    )
    puzzle = parse_puzzle(sample)
    assert part1(puzzle) == 21
    assert part2(puzzle) == 8


if __name__ == "__main__":
    tests()
    puzzle = parse_puzzle(l.strip() for l in open("input").readlines())
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2: {}".format(part2(puzzle)))
