# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/3 """

import time
from collections import Counter

def load_input(filename):
    return [x.strip() for x in open(filename, "r").readlines()]


def solve_part_one(input):
    gamma_rate = "".join([Counter(column).most_common()[0][0] for column in zip(*input)])
    epsilon_rate = "".join([Counter(column).most_common()[-1][0] for column in zip(*input)])
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def solve_part_two(input):
    remaining = input
    pos = 0
    while len(remaining) > 1:
        most_common = find_most_common(remaining, pos)
        remaining = filter(remaining, pos, most_common)
        pos += 1
    oxygen_generator = remaining[0]

    remaining = input
    pos = 0
    while len(remaining) > 1:
        least_common = find_least_common(remaining, pos)
        remaining = filter(remaining, pos, least_common)
        pos += 1
    co2_rating = remaining[0]

    return int(oxygen_generator, 2) * int(co2_rating, 2)


def filter(input, pos, value):
    return [line for line in input if line[pos] == value]


def find_most_common(input, pos):
    mc = Counter(list(zip(*input))[pos]).most_common()
    if mc[0][1] == mc[-1][1]:
        return '1'
    else:
        return mc[0][0]
    total = 0
    for line in input:
        char = line[pos]
        total += int(char)
    if total >= len(input) / 2:
        return "1"
    return "0"


def find_least_common(input, pos):
    return '0' if find_most_common(input, pos) == '1' else '1'


if __name__ == "__main__":
    start_time = time.time()

    # input_file = '2021_day_03_input_sample.txt'
    input_file = "2021_day_03_input.txt"
    input = load_input(input_file)

    """Part One"""
    result = solve_part_one(input)
    print(f"Day 3 Part One: {result}")

    """Part Two"""
    result = solve_part_two(input)
    print(f"Day 3 Part Two: {result}")

    print("--- %.2f seconds ---" % (time.time() - start_time))
