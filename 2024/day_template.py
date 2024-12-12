"""
Advent of Code 2024

https://adventofcode.com/2024/day/X

"""

from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf

DAY = "XX"


def read_input(input_filename: str) -> Any:
    with open(input_filename, "r") as file:
        return file.read().splitlines()


def part_A(input_filename: str) -> int:
    return 0


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    # input_filename = f"day_{DAY}_input.txt"

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
