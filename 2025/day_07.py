"""
Advent of Code 2025
--- Day 7: Laboratories ---
https://adventofcode.com/2025/day/7

This process continues until all of the tachyon beams reach a splitter or exit the manifold:

.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|

"""

from functools import lru_cache
from typing import List, Set

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "07"


def read_input(input_filename: str) -> List[Set[int]]:
    with open(input_filename, "r") as file:
        data: List[Set[int]] = []
        for line in file.read().splitlines():
            if arr_line := {i for i, char in enumerate(line) if char != "."}:
                data.append(arr_line)
    return data


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    beam_positions: Set[int] = data[0].copy()
    count_split = 0
    for row in data[1:]:
        new_beam_positions = set()
        for beam in beam_positions:
            if beam in row:
                new_beam_positions.update([beam - 1, beam + 1])
                count_split += 1
            else:
                new_beam_positions.add(beam)
        beam_positions = new_beam_positions

    return count_split


def solve_part_b(data: List[Set[int]]) -> int:

    @lru_cache(maxsize=None)
    def count_timelines(beam_position: int, row_index: int) -> int:
        if row_index >= len(data):
            return 1

        row = data[row_index]
        if beam_position in row:
            return count_timelines(beam_position - 1, row_index + 1) + count_timelines(
                beam_position + 1, row_index + 1
            )
        else:
            return count_timelines(beam_position, row_index + 1)

    initial_positions = data[0]
    total = 0
    for pos in initial_positions:
        total += count_timelines(pos, 1)
    return total


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    return solve_part_b(data)


def main() -> None:
    download_input(DAY, 2025)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Answer: 1635

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Answer: 58097428661390


if __name__ == "__main__":
    main()
