"""
Advent of Code 2025

https://adventofcode.com/2025/day/3

"""

from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "03"


def read_input(input_filename: str) -> List[List[int]]:
    with open(input_filename, "r") as file:
        return [list(map(int, line)) for line in file.read().splitlines()]


def max_power_with_two(line: List[int]) -> int:
    max_in_line = max(line[:-1])
    pos_of_max = line.index(max_in_line)
    next_max = max(line[pos_of_max + 1 :])
    return max_in_line * 10 + next_max


# # Old version with simpler logic but less efficient (O(K * N)).
# def max_power_general(line: List[int], nb_digits: int = 12) -> int:
#     digits: List[int] = []
#     position = 0
#     for i in range(nb_digits - 1, -1, -1):
#         if i > 0:
#             max_in_line = max(line[position:-i])
#         else:
#             max_in_line = max(line[position:])
#         digits.append(max_in_line)
#         position = line.index(max_in_line, position) + 1
#     return int("".join(map(str, digits)))


# New version with monotonic-stack logic (O(N)).
def max_power_general(line: List[int], nb_digits: int = 12) -> int:
    stack: List[int] = []
    n = len(line)
    for i, digit in enumerate(line):
        while stack and stack[-1] < digit and len(stack) + (n - i) > nb_digits:
            stack.pop()
        if len(stack) < nb_digits:
            stack.append(digit)
    return int("".join(map(str, stack)))


def part_A(input_filename: str) -> int:
    grid = read_input(input_filename)
    total = 0
    for line in grid:
        total += max_power_with_two(line)
    return total


def part_B(input_filename: str) -> int:
    grid = read_input(input_filename)
    total = 0
    for line in grid:
        total += max_power_general(line)
    return total


def main() -> None:
    download_input(DAY, 2025)
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
