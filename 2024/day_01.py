"""
Advent of Code 2024
--- Day 1: Historian Hysteria ---
https://adventofcode.com/2024/day/1
"""

import re
from collections import Counter
from typing import Any, Callable, Dict, List, Tuple

from aoc_performance import aoc_perf
from aoc_utils import compose, download_input

DAY = "01"


def read_input(filename: str) -> Tuple[List[int], List[int]]:
    left: List[int] = []
    right: List[int] = []
    with open(filename, "r") as f:
        for line in f:
            left_item, right_item = line.split("   ")
            left.append(int(left_item))
            right.append(int(right_item))
    return left, right


def part_A(input_filename: str) -> int:
    left, right = read_input(input_filename)
    left.sort()
    right.sort()

    return sum(abs(left_item - right_item) for left_item, right_item in zip(left, right))


def part_B(input_filename: str) -> int:
    left, right = read_input(input_filename)
    map_count = Counter(right)
    return sum(item * map_count.get(item, 0) for item in left)


def main() -> None:
    download_input(DAY, 2024)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
