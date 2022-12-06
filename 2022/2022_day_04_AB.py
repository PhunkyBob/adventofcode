# -*- coding: utf-8 -*-
""" 
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4 

For example, consider the following list of section assignment pairs:
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
"""
DAY = "04"

from aoc_performance import aoc_perf


def get_assignments(input: str) -> set:
    """Assignment format:
    from-to
    Ex:
    10-13
    means
    10, 11, 12, 13
    """
    from_idx, to_idx = map(lambda x: int(x), input.split("-"))
    assignment = set(i for i in range(from_idx, to_idx + 1))
    return assignment


def part_one(filename: str) -> int:
    total_count = 0
    with open(filename, "r") as f:
        for line in map(lambda x: x.strip(), f):
            left, right = map(get_assignments, line.split(","))
            len_intersection = len(left.intersection(right))
            if len_intersection == min(len(left), len(right)):
                total_count += 1
    return total_count


def part_two(filename: str) -> int:
    total_count = 0
    with open(filename, "r") as f:
        for line in map(lambda x: x.strip(), f):
            left, right = map(get_assignments, line.split(","))
            len_intersection = len(left.intersection(right))
            total_count += 1 if len_intersection else 0
    return total_count


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
