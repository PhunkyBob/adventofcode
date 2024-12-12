"""
Advent of Code 2024

https://adventofcode.com/2024/day/2

"""

from itertools import pairwise
from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf

DAY = "02"


def read_input(filename: str) -> List[List[int]]:
    data: List[List[int]] = []
    with open(filename, "r") as f:
        data = [list(map(int, line.split(" "))) for line in f]
    return data


def is_safe(data: List[int]) -> bool:
    min_diff = 1
    max_diff = 3
    all_decrease = all(min_diff <= (a - b) <= max_diff for a, b in pairwise(data))
    if all_decrease:
        return True
    all_increase = all(min_diff <= (b - a) <= max_diff for a, b in pairwise(data))
    return all_increase


def is_safe_but_one(data: List[int]) -> bool:
    if is_safe(data):
        return True
    return any(is_safe(data[:item_remove] + data[item_remove + 1 :]) for item_remove in range(len(data)))


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(is_safe(item) for item in data)


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(is_safe_but_one(item) for item in data)


def main() -> None:
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
