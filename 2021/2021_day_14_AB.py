# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/14 """

import time
from itertools import pairwise
from collections import Counter, defaultdict


def load_input(filename):
    with open(filename, "r") as f:
        polymer_template, pair_insertion = f.read().split("\n\n")
    return polymer_template, {
        key: val
        for key, val in [pair.split(" -> ") for pair in pair_insertion.split("\n")]
    }


def do_step_1(polymer_template, pair_insertion):
    new_pairs = []
    for a, b in pairwise(polymer_template):
        new_pairs.append(a + pair_insertion[a + b] + b)
    to_string = new_pairs[0][0] + "".join([p[1:3] for p in new_pairs])
    return to_string


def do_step_2(pairs, pair_insertion):
    new_pairs = defaultdict(int)
    for pair in pairs:
        to_insert = pair_insertion[pair]
        new_pairs[pair[0] + to_insert] += pairs[pair]
        new_pairs[to_insert + pair[1]] += pairs[pair]
    return new_pairs


def solve_part_one(polymer_template, pair_insertion, steps=10):
    new_polymer = polymer_template
    # print("Template:", new_polymer)
    for i in range(steps):
        new_polymer = do_step_1(new_polymer, pair_insertion)
        # print(f"After step {i+1}:", new_polymer)

    most_common = Counter(list(new_polymer)).most_common()
    return most_common[0][1] - most_common[-1][1]


def solve_part_two(polymer_template, pair_insertion, steps=40):
    pairs = defaultdict(int)
    for a, b in pairwise(polymer_template):
        pairs[a + b] += 1
    for _ in range(steps):
        pairs = do_step_2(pairs, pair_insertion)

    chars = defaultdict(int)
    chars[polymer_template[0]] += 1
    chars[polymer_template[-1]] += 1
    for p in pairs:
        chars[p[0]] += pairs[p]
        chars[p[1]] += pairs[p]

    most_common = Counter(chars).most_common()
    return int(most_common[0][1] / 2 - most_common[-1][1] / 2)


if __name__ == "__main__":
    start_time = time.time()

    # input_file = '2021_day_14_input_sample.txt'
    input_file = "2021_day_14_input.txt"
    polymer_template, pair_insertion = load_input(input_file)

    """Part One"""
    result = solve_part_one(polymer_template, pair_insertion)
    print(f"Day 14 Part One: {result}")

    """Part Two"""
    result = solve_part_two(polymer_template, pair_insertion)
    print(f"Day 14 Part Two: {result}")

    print("--- %.2f seconds ---" % (time.time() - start_time))
