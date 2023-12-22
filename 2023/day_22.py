"""
Advent of Code 2023
--- Day 22: Sand Slabs ---
https://adventofcode.com/2023/day/22

"""

import itertools
import re
from typing import Any, Callable, List, Dict, Set, Tuple
from aoc_performance import aoc_perf
import numpy as np

DAY = "22"

Coord = Tuple[int, int, int]
Block = Tuple[Coord, ...]
Blocks = Dict[int, Block]


def read_input(input_filename: str) -> Blocks:
    blocks: Blocks = {}
    with open(input_filename, "r") as input_file:
        input_lines = input_file.readlines()
        for index, line in enumerate(input_lines):
            res = re.match(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", line)
            if not res:
                continue
            x1, y1, z1, x2, y2, z2 = res.groups()
            blocks[index] = tuple(
                tuple(
                    itertools.product(
                        range(int(x1), int(x2) + 1),
                        range(int(y1), int(y2) + 1),
                        range(int(z1), int(z2) + 1),
                    )
                )
            )
    return blocks


def continue_fall(blocks: Blocks) -> Blocks:
    new_blocks: Blocks = {}
    sorted_blocks = sorted(blocks.keys(), key=lambda x: min(elem[2] for elem in blocks[x]))
    x_max = max(max(elem[0] for elem in blocks[block]) for block in blocks)
    y_max = max(max(elem[1] for elem in blocks[block]) for block in blocks)

    up_view = np.zeros((x_max + 1, y_max + 1), dtype=int)
    for block in sorted_blocks:
        actual_max_z = int(max(up_view[x, y] for x, y, z in blocks[block]))
        block_bottom = min(z for x, y, z in blocks[block])
        block_height = max(z for x, y, z in blocks[block]) - block_bottom + 1
        distance_to_fall = block_bottom - actual_max_z - 1
        new_blocks[block] = tuple((x, y, z - distance_to_fall) for x, y, z in blocks[block])
        new_block_top = max(z for x, y, z in new_blocks[block])
        for x, y, z in new_blocks[block]:
            up_view[x, y] = new_block_top

    return new_blocks


def part_A(input_filename: str) -> int:
    blocks = read_input(input_filename)
    new_blocks = continue_fall(blocks)
    distinct_blocks = set(blocks.values())
    belows: Dict[int, Set[int]] = {}  # block -> [blocks above]
    with aoc_perf(memory=True):
        for block_1, block_2 in itertools.permutations(new_blocks.keys(), 2):
            if block_1 == block_2:
                continue
            bottom_1 = min(z for x, y, z in new_blocks[block_1])
            top_2 = max(z for x, y, z in new_blocks[block_2])
            if bottom_1 != top_2 + 1:
                continue
            for x, y, z in new_blocks[block_1]:
                if (x, y, z - 1) in new_blocks[block_2]:
                    if block_1 not in belows:
                        belows[block_1] = set()
                    belows[block_1].add(block_2)
                    break
    are_only_support = set().union(*[val for val in belows.values() if len(val) == 1])
    return len(distinct_blocks) - len(are_only_support)


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
