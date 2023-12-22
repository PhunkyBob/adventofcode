"""
Advent of Code 2023
--- Day 6: Wait For It ---
https://adventofcode.com/2023/day/6

"""
from math import floor
from typing import Any, Callable, List, Dict, Tuple
from aoc_performance import aoc_perf
import re
from functools import reduce
import operator

DAY = "06"


def read_input(input_filename: str) -> Tuple[List[int], List[int]]:
    with open(input_filename, "r") as f:
        values = [list(map(int, re.findall(r"(\d+)", line))) for line in f.readlines()]
    return (values[0], values[1])


def read_input_part2(input_filename: str) -> Tuple[int, int]:
    with open(input_filename, "r") as f:
        values = [int("".join(re.findall(r"(\d+)", line))) for line in f.readlines()]
    return (values[0], values[1])


def count_winning_loop(time: int, distance: int) -> int:
    return sum(t * (time - t) > distance for t in range(time))


def count_winning_math(time: int, distance: int) -> int:
    discriminant = time**2 - 4 * distance

    if discriminant <= 0:
        return 0
    root1 = (time + (discriminant**0.5)) / 2
    root2 = (time - (discriminant**0.5)) / 2
    min_root = min(root1, root2)
    max_root = max(root1, root2)
    if max_root == int(max_root):
        max_root -= 1
    return abs(int(max_root) - int(min_root))


def part_A(input_filename: str) -> int:
    times, distances = read_input(input_filename)
    winnings = [count_winning_math(time, distance) for time, distance in zip(times, distances)]
    return reduce(operator.mul, winnings, 1)


def part_B(input_filename: str) -> int:
    time, distance = read_input_part2(input_filename)
    return count_winning_math(time, distance)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

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
