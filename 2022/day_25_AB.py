# -*- coding: utf-8 -*-
""" 
--- Day 25: Full of Hot Air ---
https://adventofcode.com/2022/day/25

The SNAFU brochure contains a few more examples of decimal ("normal") numbers and their SNAFU counterparts:

  Decimal          SNAFU
        1              1
        2              2
        3             1=
        4             1-
        5             10
        6             11
        7             12
        8             2=
        9             2-
       10             20
       15            1=0
       20            1-0
     2022         1=11-2
    12345        1-0---0
314159265  1121-1110-1=0

"""
DAY = "25"

from aoc_performance import aoc_perf
from typing import Dict, List

snafu_digits: Dict = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def snafu_to_int(input: str) -> int:
    return sum(snafu_digits[char] * (5**pos) for pos, char in enumerate(reversed(input.strip())))


def int_to_snafu(input: int) -> str:
    if input == 0:
        return ""
    quotient, remainder = divmod(input + 2, 5)
    return int_to_snafu(quotient) + "=-012"[remainder]


def part_one(filename: str) -> int:
    int_result = sum(map(snafu_to_int, [line.strip() for line in open(filename, "r")]))
    return int_to_snafu(int_result)


def part_two(filename: str) -> int:
    return "Merry Christmas"


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

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
