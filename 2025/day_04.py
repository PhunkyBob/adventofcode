"""
Advent of Code 2025

https://adventofcode.com/2025/day/04

"""

from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "04"

Coord = tuple[int, int]
Grid = set[Coord]

GRID: Grid = set()
HEIGHT = 0
WIDTH = 0

ACCESSIBLE_PAPPERS: Grid = set()


def read_input(input_filename: str) -> None:
    global HEIGHT, WIDTH, GRID
    with open(input_filename, "r") as file:
        lines = file.read().splitlines()
        HEIGHT = len(lines)
        WIDTH = len(lines[0])
        GRID = {(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "@"}


def print_grid() -> None:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print("@" if (x, y) in GRID else ".", end="")
        print()


def cout_pappers_around(x: int, y: int) -> int:
    return sum((x + dx, y + dy) in GRID for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0))


def count_accessible_pappers(remove: bool = False) -> int:
    global GRID
    accessibles: int = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) not in GRID:
                continue
            around = cout_pappers_around(x, y)
            if around < 4:
                accessibles += 1
                if remove:
                    GRID.remove((x, y))
    return accessibles


def part_A(input_filename: str) -> int:
    read_input(input_filename)
    # print_grid()
    return count_accessible_pappers()


def part_B(input_filename: str) -> int:
    read_input(input_filename)
    total_accessible = 0
    while accessible := count_accessible_pappers(remove=True):
        total_accessible += accessible
    return total_accessible


def main() -> None:
    download_input(DAY, 2025)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

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
