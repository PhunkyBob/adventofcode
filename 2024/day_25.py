"""
Advent of Code 2024
--- Day 25: Code Chronicle ---
https://adventofcode.com/2024/day/25

"""

from itertools import product
from typing import Any, List, Tuple

from aoc_performance import aoc_perf

DAY = "25"


def read_input(input_filename: str) -> Any:
    locks: List[Tuple[int, ...]] = []
    keys: List[Tuple[int, ...]] = []
    with open(input_filename, "r") as file:
        for item in file.read().split("\n\n"):
            elem = tuple(sum(pin == "#" for pin in pins) - 1 for pins in zip(*item.splitlines()))
            if item.startswith("#"):
                locks.append(elem)
            else:
                keys.append(elem)
    return locks, keys


def part_A(input_filename: str) -> int:
    locks, keys = read_input(input_filename)
    return sum(all((k + l <= 5 for k, l in zip(key, lock))) for lock, key in product(locks, keys))


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
