# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/2 """

import time


def solve_part_one(data):
    horizontal_position = 0
    depth = 0

    for d in data:
        action = d[0]
        value = int(d[1])
        if action == "forward":
            horizontal_position += value
        elif action == "down":
            depth += value
        elif action == "up":
            depth -= value
    return horizontal_position * depth


def solve_part_two(data):
    horizontal_position = 0
    depth = 0
    aim = 0

    for d in data:
        action = d[0]
        value = int(d[1])
        if action == "forward":
            horizontal_position += value
            depth += aim * value
        elif action == "down":
            aim += value
        elif action == "up":
            aim -= value
    return horizontal_position * depth


if __name__ == "__main__":
    start_time = time.time()

    # input_file = '2021_day_02_input_sample.txt'
    input_file = "2021_day_02_input.txt"
    input = [line.strip().split(" ") for line in open(input_file, "r").readlines()]

    """Part One"""
    result = solve_part_one(input)
    print(f"Day 02 Part One: {result}")

    """Part Two"""
    result = solve_part_two(input)
    print(f"Day 02 Part Two: {result}")

    print("--- %.2f seconds ---" % (time.time() - start_time))
