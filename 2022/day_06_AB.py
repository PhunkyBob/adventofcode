# -*- coding: utf-8 -*-
""" 
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6 

To fix the communication system, you need to add a subroutine to the device 
that detects a start-of-packet marker in the datastream. In the protocol 
being used by the Elves, the start of a packet is indicated by a sequence 
of four characters that are all different.
"""
DAY = "06"

from aoc_performance import aoc_perf
from typing import List


def read_input(filename: str):
    data: str = ""
    with open(filename, "r") as f:
        data = f.read()
    return data


def find_position(data: str, header_size: int = 4) -> int:
    first_n: List[str] = list(data[:header_size])
    pos: int = header_size
    while len(set(first_n)) != header_size:
        first_n.pop(0)
        first_n.append(data[pos])
        pos += 1
    return pos


def part_one(filename: str) -> int:
    data = read_input(filename)
    return find_position(data)


def part_two(filename: str) -> int:
    HEADER_SIZE = 14
    data = read_input(filename)
    return find_position(data, header_size=HEADER_SIZE)


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

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
