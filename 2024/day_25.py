"""
Advent of Code 2024
--- Day 25: Code Chronicle ---
https://adventofcode.com/2024/day/25

"""

from itertools import product
from typing import Any, List, Tuple

import numpy as np

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "25"


def read_input(input_filename: str):
    with open(input_filename, "r") as file:
        items = file.read().split("\n\n")
        locks = np.array(
            [
                [sum(pin == "#" for pin in pins) - 1 for pins in zip(*item.splitlines())]
                for item in items
                if item.startswith("#")
            ]
        )
        keys = np.array(
            [
                [sum(pin == "#" for pin in pins) - 1 for pins in zip(*item.splitlines())]
                for item in items
                if not item.startswith("#")
            ]
        )
    return locks, keys


def part_A(input_filename: str) -> int:
    locks, keys = read_input(input_filename)
    return int(np.sum(np.all(keys[:, np.newaxis] + locks <= 5, axis=2)))


def main() -> None:
    download_input(DAY, 2024)
    # input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
