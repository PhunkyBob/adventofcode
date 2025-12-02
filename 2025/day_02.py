"""
Advent of Code 2025

https://adventofcode.com/2025/day/2

Input sample:
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs.

Adding up all the invalid IDs in this example produces 1227775554.
"""

import re
from typing import Any, Callable, Dict, List, Tuple

from aoc_performance import aoc_perf

DAY = "02"

MyRange = Tuple[int, int]


def read_input(input_filename: str) -> List[MyRange]:
    with open(input_filename, "r") as file:
        return [tuple(map(int, r.split("-")[0:2])) for r in file.read().split(",")]  # type: ignore


def get_invalid_total_in_range_part_A(my_range: MyRange) -> int:
    invalid: int = 0
    i = my_range[0]
    while i <= my_range[1]:
        if len(str(i)) % 2 == 1:
            # Nombre de chiffres impair, on passe directement au prochain nombre avec un nombre pair de chiffres
            digits = len(str(i))
            i = 10**digits
            continue
        str_i = str(i)
        mid = len(str_i) // 2
        left = str_i[:mid]
        right = str_i[mid:]
        if left == right:
            invalid += i
        i += 1
    return invalid


def get_invalid_total_in_range_part_B(my_range: MyRange) -> int:
    invalid: int = 0
    for i in range(my_range[0], my_range[1] + 1):
        str_i = str(i)
        # Vérifie si la chaîne entière est composée d'un motif répété au moins 1 fois
        if re.fullmatch(r"(\d+)\1+", str_i):
            invalid += i
    return invalid


def part_A(input_filename: str) -> int:
    ranges: List[MyRange] = read_input(input_filename)
    return sum(get_invalid_total_in_range_part_A(r) for r in ranges)


def part_B(input_filename: str) -> int:
    ranges: List[MyRange] = read_input(input_filename)
    return sum(get_invalid_total_in_range_part_B(r) for r in ranges)


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Answer: 23534117921

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Answer: 31755323497


if __name__ == "__main__":
    main()
