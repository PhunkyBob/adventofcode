"""
Advent of Code 2023
--- Day 22: Sand Slabs ---
https://adventofcode.com/2023/day/22

"""

import heapq
import itertools
import re
from typing import Dict, Set, Tuple
from aoc_performance import aoc_perf

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

    # For each block, find the actual max z
    up_view = [[0 for _ in range(y_max + 1)] for _ in range(x_max + 1)]
    for block in sorted_blocks:
        actual_max_z = int(max(up_view[x][y] for x, y, z in blocks[block]))
        block_bottom = min(z for _, _, z in blocks[block])
        distance_to_fall = block_bottom - actual_max_z - 1
        new_blocks[block] = tuple((x, y, z - distance_to_fall) for x, y, z in blocks[block])
        new_block_top = max(z for _, _, z in new_blocks[block])
        for x, y, _ in new_blocks[block]:
            up_view[x][y] = new_block_top

    return new_blocks


def get_above_belows(new_blocks: Blocks) -> Tuple[Dict[int, Set[int]], Dict[int, Set[int]]]:
    belows: Dict[int, Set[int]] = {}  # block -> [blocks below]
    aboves: Dict[int, Set[int]] = {}  # block -> [blocks above]
    unit_blocks = {b: key for key, blocks in new_blocks.items() for b in blocks}
    for a_coord, a_block in unit_blocks.items():
        if (a_coord[0], a_coord[1], a_coord[2] - 1) in unit_blocks:
            b_block = unit_blocks[(a_coord[0], a_coord[1], a_coord[2] - 1)]
            if b_block == a_block:
                continue
            if a_block not in belows:
                belows[a_block] = set()
            belows[a_block].add(b_block)
            if b_block not in aboves:
                aboves[b_block] = set()
            aboves[b_block].add(a_block)
    return aboves, belows


def part_A(input_filename: str) -> int:
    blocks = read_input(input_filename)
    new_blocks = continue_fall(blocks)
    _, belows = get_above_belows(new_blocks)
    are_only_support = set().union(*[val for val in belows.values() if len(val) == 1])
    return len(blocks) - len(are_only_support)


def count_falling(block_id: int, aboves, belows) -> int:
    heapq.heapify(queue := [block_id])
    count = 0
    already_removed: Set[int] = set()
    while queue:
        if (block := heapq.heappop(queue)) in already_removed:
            continue
        already_removed.add(block)
        if block not in aboves:
            continue
        for block in aboves[block]:
            if belows[block] - already_removed == set():
                heapq.heappush(queue, block)
                count += 1
    return count


def part_B(input_filename: str) -> int:
    blocks = read_input(input_filename)
    new_blocks = continue_fall(blocks)
    aboves, belows = get_above_belows(new_blocks)
    are_only_support = set().union(*[val for val in belows.values() if len(val) == 1])

    return sum(count_falling(support, aboves, belows) for support in are_only_support)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected answer : 497

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected answer : 67468


if __name__ == "__main__":
    main()
