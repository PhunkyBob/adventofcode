# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/10 """

import time

brackets = {"{": "}", "[": "]", "(": ")", "<": ">"}
illegal_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete_points = {")": 1, "]": 2, "}": 3, ">": 4}


def load_input(filename):
    return [x.strip() for x in open(filename, "r").readlines()]


def is_only_open_brackets(line):
    return sum([1 for char in line if char not in brackets]) == 0


def remove_brackets(line):
    previous = ""
    while previous != line:
        previous = line
        for key in brackets:
            line = line.replace(key + brackets[key], "")
    return line


def get_first_closing_bracket(line):
    for char in line:
        if char in brackets.values():
            return char


def get_closing_brackets(line):
    result = [brackets[c] for c in reversed(list(line))]
    return result


def solve_part_one(input):
    result = 0
    for line in input:
        stripped = remove_brackets(line)
        if not is_only_open_brackets(stripped):
            result += illegal_points[get_first_closing_bracket(stripped)]
    return result


def solve_part_two(input):
    results = []
    for line in input:
        stripped = remove_brackets(line)
        if is_only_open_brackets(stripped):
            closing = get_closing_brackets(stripped)
            result = 0
            for char in closing:
                result *= 5
                result += autocomplete_points[char]
            results.append(result)
    results = sorted(results)
    return results[len(results) // 2]


if __name__ == "__main__":
    start_time = time.time()

    # input_file = "2021_day_10_input_sample.txt"
    input_file = "2021_day_10_input.txt"
    input = load_input(input_file)

    """Part One"""
    result = solve_part_one(input)
    print(f"Day 10 Part One: {result}")
    # Your puzzle answer was 315693.

    """Part Two"""
    result = solve_part_two(input)
    print(f"Day 10 Part Two: {result}")
    # Your puzzle answer was 1870887234.

    print("--- %.2f seconds ---" % (time.time() - start_time))
