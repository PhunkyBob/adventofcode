# -*- coding: utf-8 -*-
""" 
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7

Perhaps you can delete some files to make space for the update?
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

The total sizes of the directories above can be found as follows:
- The total size of directory e is 584 because it contains a single file 
i of size 584 and no other directories.
- The directory a has total size 94853 because it contains files f (size 
29116), g (size 2557), and h.lst (size 62596), plus file i indirectly 
(a contains e which contains i).
- Directory d has total size 24933642.
- As the outermost directory, / contains every file. Its total size is 
48381165, the sum of the size of every file.
"""
DAY = "07"

from aoc_performance import aoc_perf
from collections import defaultdict
from functools import lru_cache

folders = defaultdict(lambda: {"files": {}, "folders": {}})


@lru_cache
def calculate_total_size(starts_with: str) -> int:
    size_dir = sum(folders[starts_with]["files"].values())
    size_sub_dir = 0
    for dir in folders[starts_with]["folders"]:
        size_sub_dir += calculate_total_size(f"{starts_with}/{dir}")
    return size_dir + size_sub_dir


def init_folders(filename: str) -> None:
    global folders
    folders = defaultdict(lambda: {"files": {}, "folders": {}})
    current_folder = []
    with open(filename, "r") as f:
        for line in map(lambda x: x.strip(), f):
            if line.startswith("$ cd"):
                _, command, parameter = line.split(" ")
                if command == "cd":
                    if parameter == "..":
                        current_folder.pop()
                    elif parameter == "/":
                        current_folder = ["/"]
                    else:
                        current_folder.append(parameter)
            elif line[0].startswith("$"):
                pass
            else:
                size, name = line.split(" ")
                if size == "dir":
                    folders["/".join(current_folder)]["folders"][name] = 0
                if size.isnumeric():
                    folders["/".join(current_folder)]["files"][name] = int(size)


def part_one(filename: str) -> int:
    AT_MOST = 100000
    init_folders(filename)
    answer = 0
    for folder in folders:
        size = calculate_total_size(folder)
        if size < AT_MOST:
            answer += size
    return answer


def part_two(filename: str) -> int:
    TOTAL_DISK_SPACE = 70000000
    UNUSED_SPACE_NEEDED = 30000000
    init_folders(filename)
    root_size = calculate_total_size("/")
    available_disk_space = TOTAL_DISK_SPACE - root_size
    min_folder, min_folder_size = "/", root_size
    for folder in folders:
        size = calculate_total_size(folder)
        if available_disk_space + size > UNUSED_SPACE_NEEDED:
            if size < min_folder_size:
                min_folder, min_folder_size = folder, size
    return min_folder, min_folder_size


def main() -> None:
    input_filename = f"2022_day_{DAY}_input_sample.txt"
    input_filename = f"2022_day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
