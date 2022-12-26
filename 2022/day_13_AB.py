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
import functools
from itertools import chain


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
    items: List
    debug: bool

    def __init__(self, filename, debug: bool = False) -> None:
        self.items = []
        self.debug = debug
        with open(filename, "r") as f:
            for pair in f.read().split("\n\n"):
                pair = PairOfPacket(pair.strip(), debug)
                self.items.append(pair.left)
                self.items.append(pair.right)

    def is_right_order(self, index: int) -> bool:
        if self.debug:
            print(f"== Pair {index+1} ==")
        return DistressSignal.is_smaller(self.items[index * 2], self.items[index * 2 + 1], debug=self.debug)

    @staticmethod
    def is_smaller(left: int | List, right: int | List, space: int = 0, debug=False) -> bool:
        space_filler = " " * space * 2
        DistressSignal.print_debug(f"{space_filler}- Compare {left} vs {right}", debug)
        if type(left) == int and type(right) == list:
            DistressSignal.print_debug(
                f"{space_filler}- Mixed types; convert left to [{left}] and retry comparison", debug
            )
            return DistressSignal.is_smaller([left], right, space + 1, debug)
        if type(left) == list and type(right) == int:
            DistressSignal.print_debug(
                f"{space_filler}- Mixed types; convert right to [{right}] and retry comparison", debug
            )
            return DistressSignal.is_smaller(left, [right], space + 1, debug)
        for index in range(min(len(left), len(right))):
            left_item, right_item = left[index], right[index]
            if type(left_item) == int and type(right_item) == int:
                DistressSignal.print_debug(f"{space_filler}- Compare {left_item} vs {right_item}", debug)
                if left_item < right_item:
                    DistressSignal.print_debug(
                        f"{space_filler}- Left side is smaller, so inputs are in the right order", debug
                    )
                    return True
                elif right_item < left_item:
                    DistressSignal.print_debug(
                        f"{space_filler}- Right side is smaller, so inputs are NOT in the right order", debug
                    )
                    return False
                else:
                    continue
            else:
                res = DistressSignal.is_smaller(left_item, right_item, space + 1, debug)
                if res in [True, False]:
                    return res
        if len(left) < len(right):
            DistressSignal.print_debug(
                f"{space_filler}- Left side ran out of items, so inputs are in the right order", debug
            )
            return True
        if len(left) > len(right):
            DistressSignal.print_debug(
                f"{space_filler}- Right side ran out of items, so inputs are NOT in the right order", debug
            )
            return False
        return "?"

    @staticmethod
    def print_debug(string: str, debug: bool = True) -> None:
        if debug:
            print(string)


def part_one(filename: str) -> int:
    data = DistressSignal(filename, False)
    return sum(i + 1 for i in range(len(data.items) // 2) if data.is_right_order(i))


def part_two(filename: str) -> int:
    FIRST_DIVIDER = [[2]]
    SECOND_DIVIDER = [[6]]
    data = DistressSignal(filename, False)
    compare = lambda x, y: -1 if DistressSignal.is_smaller(x, y) else 1
    res = sorted(list(chain(data.items, [FIRST_DIVIDER], [SECOND_DIVIDER])), key=functools.cmp_to_key(compare))
    index_1 = res.index(FIRST_DIVIDER)
    index_2 = res.index(SECOND_DIVIDER)
    return (index_1 + 1) * (index_2 + 1)


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
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
