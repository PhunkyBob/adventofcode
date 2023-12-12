"""
Advent of Code 2023

https://adventofcode.com/2023/day/12

"""
from functools import lru_cache
from typing import Any, Callable, List, Dict, Tuple
from aoc_performance import aoc_perf
import re

DAY = "12"


@lru_cache
def count_possible(input: str, pattern: str) -> int:
    new_pattern = r"(\.|\?)+".join([r"(#|\?)" * int(i) for i in pattern.split(",")])
    new_pattern = r"^(\.|\?)*" + new_pattern + r"(\.|\?)*$"
    if re.match(new_pattern, input):
        if "?" in input:
            return count_possible(input.replace("?", ".", 1), pattern) + count_possible(
                input.replace("?", "#", 1), pattern
            )
        else:
            # print(input)
            return 1
    return 0


def unfold(input: str, pattern: str) -> Tuple[str, str]:
    new_input = "?".join([input] * 5)
    new_patter = ",".join([pattern] * 5)
    return new_input, new_patter


def read_input(input_filename: str) -> List[Tuple[str, str]]:
    with open(input_filename, "r") as input_file:
        return [tuple(line.strip().split(" ")) for line in input_file]


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(count_possible(d[0], d[1]) for d in data)


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

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
