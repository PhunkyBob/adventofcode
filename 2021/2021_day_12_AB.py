# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/12 """

import time
from collections import defaultdict

all_paths = []
connections = defaultdict(lambda: [])


def load_input(filename):
    with open(filename, "r") as f:
        for line in f:
            frm, to = line.strip().split("-")
            connections[frm].append(to)
            connections[to].append(frm)
    return connections


def find_paths_1(current, previous):
    if current == current.lower() and current in previous:
        return False

    if current == "end":
        all_paths.append(previous + [current])
        return True

    for next in connections[current]:
        find_paths_1(next, previous + [current])


def find_paths_2(current, previous, visited_twice=False):
    if current == "start" and previous:
        return False
    if current.lower() == current and current in previous:
        if visited_twice:
            return False
        else:
            visited_twice = True
    if current == "end":
        all_paths.append(previous + [current])
        return True

    for next in connections[current]:
        find_paths_2(next, previous + [current], visited_twice)


def solve_part_one():
    all_paths.clear()
    # find_paths_1("start", [])
    find_paths_2("start", [], True)
    return len(all_paths)


def solve_part_two():
    all_paths.clear()
    find_paths_2("start", [])

    return len(all_paths)


if __name__ == "__main__":
    start_time = time.time()

    # input_file = "2021_day_12_input_sample.txt"
    # input_file = "2021_day_12_input_sample2.txt"
    # input_file = "2021_day_12_input_sample3.txt"
    input_file = "2021_day_12_input.txt"
    connections = load_input(input_file)

    """Part One"""
    result = solve_part_one()
    print(f"Day 12 Part One: {result}")
    # Your puzzle answer was 4411.

    """Part Two"""
    result = solve_part_two()
    print(f"Day 12 Part Two: {result}")
    # Your puzzle answer was 136767.

    print("--- %.2f seconds ---" % (time.time() - start_time))
