"""
Advent of Code 2024
--- Day 3: Mull It Over ---
https://adventofcode.com/2024/day/3

Input : xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
mul(44,46) multiplies 44 by 46 to get a result of 2024
There are also many invalid characters that should be ignored.
"""

import re
from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf

DAY = "03"


def read_input(filename: str) -> str:
    data = ""
    with open(filename, "r") as f:
        data = f.read()
    return data


def scan(data: str) -> int:
    return sum(int(a) * int(b) for a, b in res) if (res := re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)) else 0


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    return scan(data)


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    do_list = data.split("do()")
    # Everything after the "don't()" doesn't matter
    return sum(scan(do.split("don't()")[0]) for do in do_list)


def main() -> None:
    input_filename = f"day_{DAY}_input_sample_B.txt"
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
