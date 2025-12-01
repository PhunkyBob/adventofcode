"""
Advent of Code 2025

https://adventofcode.com/2025/day/X

"""

from typing import Any, Callable, Dict, List, Tuple

from aoc_performance import aoc_perf

DAY = "01"

Instruction = Tuple[str, int]


def read_input(input_filename: str) -> List[Instruction]:
    with open(input_filename, "r") as file:
        return [(line[0], int(line[1:])) for line in file.read().splitlines()]


def move_part_A(position: int, action: str, value: int) -> Tuple[int, int]:
    if action == "L":
        position -= value
    elif action == "R":
        position += value
    position %= 100
    return position, int(position == 0)


def move_part_B(position: int, action: str, value: int) -> Tuple[int, int]:
    dial_pointing_zero = 0
    if action == "L":
        dial_pointing_zero += value // 100
        dial_pointing_zero += 1 if position != 0 and position - (value % 100) <= 0 else 0
        position -= value
    elif action == "R":
        dial_pointing_zero = (position + value) // 100
        position += value
    position %= 100
    return position, dial_pointing_zero


def part_A(input_filename: str) -> int:
    instructions = read_input(input_filename)
    position = 50
    dial_pointing_zero = 0
    for action, value in instructions:
        position, dz = move_part_A(position, action, value)
        dial_pointing_zero += dz
    return dial_pointing_zero


def part_B(input_filename: str) -> int:
    instructions = read_input(input_filename)
    position = 50
    dial_pointing_zero = 0
    for action, value in instructions:
        position, dz = move_part_B(position, action, value)
        dial_pointing_zero += dz

    return dial_pointing_zero


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Answer: 1105

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Answer: 6599


if __name__ == "__main__":
    main()
