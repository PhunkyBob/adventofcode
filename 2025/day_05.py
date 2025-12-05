"""
Advent of Code 2025

https://adventofcode.com/2025/day/5

"""

import bisect
from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "05"

Range = tuple[int, int]


def read_input(input_filename: str) -> tuple[List[Range], List[int]]:
    with open(input_filename, "r") as file:
        fresh_ranges_txt, available_ingredients_txt = file.read().split("\n\n")
        fresh_ranges = [tuple(map(int, range.split("-"))) for range in fresh_ranges_txt.splitlines()]
        available_ingredients = [int(line) for line in available_ingredients_txt.splitlines()]
        return fresh_ranges, available_ingredients  # type: ignore


def sort_ranges(ranges: List[Range]) -> List[Range]:
    return sorted(ranges, key=lambda x: x[0])


def merge_ranges(sorted_ranges: List[Range]) -> List[Range]:
    if not sorted_ranges:
        return []

    merged_ranges: List[Range] = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        if start <= last_end + 1:  # +1 pour fusionner ranges adjacents
            merged_ranges[-1] = (last_start, max(last_end, end))
        else:
            merged_ranges.append((start, end))
    return merged_ranges


def count_fresh_ingredients_part_B(merged_ranges: List[Range]) -> int:
    return sum(end - start + 1 for start, end in merged_ranges)


def part_A(input_filename: str) -> int:
    fresh_ranges, available_ingredients = read_input(input_filename)
    count_fresh = 0
    for ingredient in available_ingredients:
        for start, end in fresh_ranges:
            if start <= ingredient <= end:
                count_fresh += 1
                break
    return count_fresh


def part_B(input_filename: str) -> int:
    fresh_ranges, _ = read_input(input_filename)
    sorted_ranges = sort_ranges(fresh_ranges)
    merged_ranges = merge_ranges(sorted_ranges)
    return count_fresh_ingredients_part_B(merged_ranges)


def main() -> None:
    download_input(DAY, 2025)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Answer: 761

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Answer: 345755049374932


if __name__ == "__main__":
    main()
