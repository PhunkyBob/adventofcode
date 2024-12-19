"""
Advent of Code 2024
--- Day 19: Linen Layout ---
https://adventofcode.com/2024/day/19

r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

from collections import deque
from functools import lru_cache
from typing import Any, Callable, Dict, List, Set, Tuple
import re
from trie import Trie
from aoc_performance import aoc_perf

DAY = "19"


def read_input(input_filename: str) -> Tuple[List[str], List[str]]:
    with open(input_filename, "r") as file:
        patterns, designs_text = file.read().split("\n\n")
        return patterns.split(", "), designs_text.splitlines()


def create_regex(patterns: List[str]) -> str:
    return "^(" + "|".join(patterns) + ")+$"


def is_possible(patterns: List[str], design: str) -> bool:
    filtered_patterns = [pattern for pattern in patterns if pattern in design]
    must_start = ""
    queue: deque = deque()
    queue.append((must_start, design))
    visited = set()
    while queue:
        must_start, design = queue.pop()
        if not design:
            return True
        if (must_start, design) in visited:
            continue
        visited.add((must_start, design))
        for pattern in filtered_patterns:
            if design.startswith(pattern) and (pattern, design[len(pattern) :]) not in visited:
                queue.append((pattern, design[len(pattern) :]))
    return False


@lru_cache
def is_possible_recursive(patterns: Tuple[str], design: str) -> int:
    if not design:
        return 1
    return sum(
        is_possible_recursive(patterns, design[len(pattern) :]) for pattern in patterns if design.startswith(pattern)
    )


def part_A(input_filename: str) -> int:
    patterns, designs = read_input(input_filename)
    return sum(is_possible(patterns, design) for design in designs)


def part_B(input_filename: str) -> int:
    patterns, designs = read_input(input_filename)
    total = 0
    for design in designs:
        filtered_patterns = tuple(pattern for pattern in patterns if pattern in design)
        cnt = is_possible_recursive(filtered_patterns, design)
        # print(i, cnt)
        total += cnt
    return total


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
