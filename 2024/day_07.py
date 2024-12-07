"""
Advent of Code 2024
--- Day 7: Bridge Repair ---
https://adventofcode.com/2024/day/7

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.
"""

from typing import List, Tuple

from aoc_performance import aoc_perf

DAY = "07"
Line = Tuple[int, List[int]]


def parse_line(line: str) -> Line:
    result, items = line.split(":")
    return int(result), [int(item) for item in items.split()]


def read_input(input_filename: str) -> List[Line]:
    with open(input_filename, "r") as file:
        return [parse_line(line) for line in file.readlines()]


def is_possibly_true_A(result: int, start: int, items: Tuple[int, ...]) -> bool:
    # v1 implementation: pass the following items to the next recursive call
    if result < start:
        return False
    if not items:
        return result == start
    if start == 0:
        new_start = items[0]
        new_items = items[1:]
        return is_possibly_true_A(result, new_start, new_items)
    new_element = items[0]
    new_items = items[1:]
    return is_possibly_true_A(result, start + new_element, new_items) or is_possibly_true_A(
        result, start * new_element, new_items
    )


def is_possibly_true_B(expected_result: int, items: Tuple[int, ...]) -> bool:
    # v2 implementation: don't copy items, pass the index to the next recursive call
    def is_possibly_true(index: int, value: int) -> bool:
        if expected_result < value:
            return False
        if index == len(items):
            return expected_result == value
        new_element = items[index]
        return (
            is_possibly_true(index + 1, value + new_element)
            or is_possibly_true(index + 1, value * new_element)
            or is_possibly_true(index + 1, int(f"{value}{new_element}"))
        )

    return is_possibly_true(1, items[0])


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(result for result, items in data if is_possibly_true_A(result, 0, tuple(items)))


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(result for result, items in data if is_possibly_true_B(result, tuple(items)))


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
