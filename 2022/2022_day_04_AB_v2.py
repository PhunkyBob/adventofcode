# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/4 """
DAY = "04"

from aoc_performance import aoc_perf


def part_one(filename: str) -> int:
    total_count = 0
    with open(filename, "r") as f:
        for line in f:
            left_from, left_to, right_from, right_to = map(int, line.replace("-", ",").split(","))
            if left_from <= right_from <= right_to <= left_to or right_from <= left_from <= left_to <= right_to:
                total_count += 1

    return total_count


def part_two(filename: str) -> int:
    total_count = 0
    with open(filename, "r") as f:
        for line in f:
            left_from, left_to, right_from, right_to = map(int, line.replace("-", ",").split(","))
            if left_from <= right_to and right_from <= left_to:
                total_count += 1
    return total_count


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
