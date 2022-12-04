# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/X """
DAY = "xx"

from aoc_performance import aoc_perf


def read_input(filename: str):
    data = []
    with open(filename, "r") as f:
        for line in map(lambda x: x.strip(), f):
            ...
            data.append(line)
    return data


def part_one(filename: str) -> int:
    data = read_input(filename)
    # Code
    return


def part_two(filename: str) -> int:
    data = read_input(filename)
    # Code
    return


def main() -> None:
    input_filename = f"2022_day_{DAY}_input_sample.txt"
    input_filename = f"2022_day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
