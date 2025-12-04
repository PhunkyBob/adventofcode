"""
Advent of Code 2025
--- Day 4: Printing Department ---

https://adventofcode.com/2025/day/04

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

The forklifts can only access a roll of paper if there are fewer
than four rolls of paper in the eight adjacent positions. If you
can figure out which rolls of paper the forklifts can access,
they'll spend less time looking and more time breaking down the
wall to the cafeteria.
"""

from collections import deque
from typing import Dict, Set, Tuple

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "04"

Coord = Tuple[int, int]
Grid = Set[Coord]
GridWithDegrees = Dict[Coord, int]


def read_input(input_filename: str) -> Grid:
    with open(input_filename, "r") as file:
        lines = file.read().splitlines()
        return {(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "@"}


def count_neighbors(x: int, y: int, grid: Grid | GridWithDegrees) -> int:
    return sum((dx != 0 or dy != 0) and ((x + dx, y + dy) in grid) for dy in (-1, 0, 1) for dx in (-1, 0, 1))


def part_A(input_filename: str) -> int:
    grid = read_input(input_filename)
    return sum(count_neighbors(x, y, grid) < 4 for x, y in grid)


def part_B(input_filename: str) -> int:
    grid = read_input(input_filename)

    # Precompute degrees
    degrees: GridWithDegrees = {}
    queue = deque()

    # Only need to track degrees for items in the grid
    for x, y in grid:
        deg = count_neighbors(x, y, grid)
        degrees[(x, y)] = deg
        if deg < 4:
            queue.append((x, y))
    removed_count = 0

    while queue:
        x, y = queue.popleft()

        # Check if already processed/removed
        if (x, y) not in degrees:
            continue

        # Remove
        del degrees[(x, y)]
        removed_count += 1

        # Update neighbors
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if (dx != 0 or dy != 0) and (nx, ny) in degrees:
                    deg = count_neighbors(nx, ny, degrees)
                    if deg < 4:
                        queue.append((nx, ny))

    return removed_count


def main() -> None:
    download_input(DAY, 2025)
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Answer: 1553

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Answer: 8442


if __name__ == "__main__":
    main()
