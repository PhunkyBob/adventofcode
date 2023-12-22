"""
Advent of Code 2023
--- Day 9: Mirage Maintenance ---
https://adventofcode.com/2023/day/9

For example:
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45

To extrapolate, start by adding a new zero to the end of your list of zeroes; because the zeroes represent differences between the two values above them, this also means there is now a placeholder in every sequence above it:
0   3   6   9  12  15   B
  3   3   3   3   3   A
    0   0   0   0   0

"""
from typing import List
from aoc_performance import aoc_perf

DAY = "09"


def get_sequence(values: List[int]) -> List[List[int]]:
    if all(v == 0 for v in values):
        return [values]
    new_values = [right - left for left, right in zip(values, values[1:])]
    return [values, *get_sequence(new_values)]


def get_last_extrapolated_value(values: List[List[int]]) -> int:
    extrapolated_value = 0
    for line in values[::-1]:
        extrapolated_value = line[-1] + extrapolated_value
    return extrapolated_value


def get_first_extrapolated_value(values: List[List[int]]) -> int:
    extrapolated_value = 0
    for line in values[::-1]:
        extrapolated_value = line[0] - extrapolated_value
    return extrapolated_value


def read_input(input_filename: str) -> List[List[int]]:
    with open(input_filename, "r") as input_file:
        return [list(map(int, line.split(" "))) for line in input_file]


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(get_last_extrapolated_value(get_sequence(line)) for line in data)


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(get_first_extrapolated_value(get_sequence(line)) for line in data)


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
