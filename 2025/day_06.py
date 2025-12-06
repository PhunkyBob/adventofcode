"""
Advent of Code 2025

https://adventofcode.com/2025/day/6

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +

So, this worksheet contains four problems:

    123 * 45 * 6 = 33210
    328 + 64 + 98 = 490
    51 * 387 * 215 = 4243455
    64 + 23 + 314 = 401

"""

import math
from typing import Any

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "06"


def read_input_part_A(input_filename: str) -> Any:
    with open(input_filename, "r") as file:
        all_lines = file.read().splitlines()
        data = []
        for line in all_lines[:-1]:
            line = map(int, filter(lambda x: x != "", line.strip().split(" ")))
            data.append(line)
        numbers = list(zip(*data))
        operators = list(filter(lambda x: x != "", all_lines[-1].strip().split(" ")))
        return numbers, operators


def read_input_part_B(input_filename: str) -> Any:
    with open(input_filename, "r") as file:
        all_lines = file.read().splitlines()
        data = []
        lines = ["".join(line).strip() for line in zip(*all_lines[:-1])]
        operators = list(filter(lambda x: x != "", all_lines[-1].strip().split(" ")))
        return lines, operators


def part_A(input_filename: str) -> int:
    numbers, operators = read_input_part_A(input_filename)
    total = 0
    for i, num in enumerate(numbers):
        if operators[i] == "*":
            total += math.prod(num)
        elif operators[i] == "+":
            total += sum(num)
    return total


def part_B(input_filename: str) -> int:
    numbers, operators = read_input_part_B(input_filename)
    operator_index = 0
    total = 0
    column_total = 0 if operators[operator_index] == "+" else 1
    for number in numbers:
        if number == "":
            total += column_total
            operator_index += 1
            column_total = 0 if operators[operator_index] == "+" else 1
            continue
        if operators[operator_index] == "*":
            column_total *= int(number)
        elif operators[operator_index] == "+":
            column_total += int(number)
            continue
    total += column_total
    return total


def main() -> None:
    download_input(DAY, 2025)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Answer: 4449991244405

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Answer: 9348430857627


if __name__ == "__main__":
    main()
