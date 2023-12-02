"""
Advent of Code 2023

https://adventofcode.com/2023/day/X

"""
from typing import Any, Callable, List, Dict
from aoc_performance import aoc_perf

DAY = "XX"


def part_A(input_filename: str) -> int:
    return 0


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
