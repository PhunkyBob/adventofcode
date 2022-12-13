# -*- coding: utf-8 -*-
""" 
--- Day 13: Distress Signal ---
https://adventofcode.com/2022/day/13 

Your list consists of pairs of packets; pairs are separated by a blank 
line. You need to identify how many pairs of packets are in the right 
order.

For example:

[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]

"""
DAY = "13"

from aoc_performance import aoc_perf
import json
from typing import List


class PairOfPacket:
    left: List
    right: List
    debug: bool

    def __init__(self, input_str: str, debug: bool = False) -> None:
        left_str, right_str = input_str.split("\n")
        self.left = json.loads(left_str)
        self.right = json.loads(right_str)
        self.debug = debug


class DistressSignal:
    pairs: List[PairOfPacket]

    def __init__(self, filename) -> None:
        self.pairs = []
        with open(filename, "r") as f:
            for pair in f.read().split("\n\n"):
                self.pairs.append(PairOfPacket(pair.strip()))

    def is_right_order(self, index: int) -> bool:
        if self.debug:
            print(f"== Pair {index+1}")
            print(f"Compare {self.pairs[index].left} vs {self.pairs[index].right}")
        self.pairs[index]

    def compare(left: int | List, right: int | List) -> bool:
        if type(left) == int and type(right) == int:
            if left < right:
                return True
            elif right < left:
                return False
            else:
                pass


def part_one(filename: str) -> int:
    data = DistressSignal(filename)
    # Code
    return


def part_two(filename: str) -> int:
    # Code
    return


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    # input_filename = f"day_{DAY}_input.txt"

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
