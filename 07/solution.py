#!/usr/bin/env python

import re


class Directory:
    def __init__(self, parent_dir=None):
        self.parent_dir = parent_dir
        self.children = dict()

    def parent(self):
        return self.parent_dir

    def child_dir(self, name):
        return self.children.setdefault(name, Directory(self))

    def add_file(self, filename, size):
        self.children[filename] = File(size)

    def size(self):
        return sum(c.size() for c in self.children.values())

    def directory_sizes(self):
        result = dict()
        for k, v in self.children.items():
            if isinstance(v, Directory):
                result[k] = v.size()
                for subdir_k, subdir_v in v.directory_sizes().items():
                    key = "/".join((k, subdir_k))
                    result[key] = subdir_v
        return result


class File:
    def __init__(self, size):
        self.filesize = int(size)

    def size(self):
        return self.filesize


def parse_puzzle(puzzlein):
    pwd = root = Directory()
    for p1, p2 in re.findall("(dir|\d+|\$ ls|\$ cd) ([^\n]+)", puzzlein):
        if p1 == "$ cd":
            if p2 == "/":
                pwd = root
            elif p2 == "..":
                pwd = pwd.parent()
            else:
                pwd = pwd.child_dir(p2)
        elif p1.isdigit():
            pwd.add_file(p2, p1)
    return root


def part1(root):
    return sum([v for v in root.directory_sizes().values() if v <= 100000])


def part2(root):
    total = 70000000
    required = 30000000
    current = total - root.size()
    min_to_delete = required - current
    return min(dir for dir in root.directory_sizes().values() if dir >= min_to_delete)


def tests():
    sample = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
    """
    puzzle = parse_puzzle(sample)
    assert part1(puzzle) == 95437
    assert part2(puzzle) == 24933642


if __name__ == "__main__":
    tests()
    puzzle = parse_puzzle(open("input").read())
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2: {}".format(part2(puzzle)))
