# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/3 """
DAY = "03"

from aoc_performance import aoc_perf
import itertools
import functools


def char_priority(char: str) -> int:
    if ord(char[0]) >= ord("a"):
        # lowercase
        return ord(char[0]) - ord("a") + 1
    else:
        # uppercase
        return ord(char[0]) - ord("A") + 27


def part_A(filename: str) -> int:
    total_score = 0
    with open(filename, "r") as f:
        # Read and strip line by line
        for line in map(lambda x: x.strip(), f):
            half = len(line) // 2
            left, right = line[:half], line[half:]
            total_score += sum(map(char_priority, set(left).intersection(right)))
    return total_score


def part_B(filename: str) -> int:
    total_score = 0
    with open(filename, "r") as f:
        # Retreive lines 3 by 3 :
        # We have 3 iterators on the same list.
        # When zip_longest, it will consume on every iteration :
        # 1st element with 1st iterator, 2nd element with 2nd iterator, 3rd w/ 3rd
        # and then return the concatenation of this 3 elements.
        packs = [iter(f)] * 3
        for pack in itertools.zip_longest(*packs):
            # Strip every lines
            pack = map(lambda x: x.strip(), pack)
            common_chars = functools.reduce(lambda i, j: i & j, (set(x) for x in pack))
            bag_score = sum(map(char_priority, common_chars))
            total_score += bag_score
        return total_score


def main() -> None:
    # input_filename = f"2022_day_{DAY}_input_sample.txt"
    input_filename = f"2022_day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
