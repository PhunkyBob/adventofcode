# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/6 """

import time
from collections import defaultdict


def load_input(filename):
    return [int(x) for x in open(filename, "r").read().strip().split(",")]


def solve_part_one(input, days=80):
    new_input = input
    for _ in range(days):
        input = new_input
        new_input = []
        for i in range(len(input)):
            value = input[i]
            if value == 0:
                new_input.append(6)
                new_input.append(8)
            else:
                new_input.append(value - 1)

    return len(new_input)


def solve_part_two(input, days=256):
    fishes = defaultdict(int, {i: input.count(i) for i in range(max(input) + 1)})

    new_fishes = fishes
    for _ in range(days):
        fishes = new_fishes
        new_fishes = defaultdict(int)
        for d in fishes:
            count = fishes[d]
            if d == 0:
                new_fishes[6] += count
                new_fishes[8] += count
            else:
                new_fishes[d - 1] += count

    return sum(new_fishes[f] for f in new_fishes)


if __name__ == "__main__":
    start_time = time.time()

    # input_file = '2021_day_06_input_sample.txt'
    input_file = "2021_day_06_input.txt"
    input = load_input(input_file)

    """Part One"""
    result = solve_part_one(input)
    print(f"Day 6 Part One: {result}")

    """Part Two"""
    result = solve_part_two(input)
    print(f"Day 6 Part Two: {result}")

    print("--- %.2f seconds ---" % (time.time() - start_time))
