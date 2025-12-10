"""
Advent of Code 2025

https://adventofcode.com/2025/day/9

"""

from functools import lru_cache
from itertools import pairwise, product
from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "09"

Coord = tuple[int, int]


def read_input(input_filename: str) -> List[Coord]:
    with open(input_filename, "r") as file:
        return [tuple(map(int, line.split(","))) for line in file.read().splitlines()]  # type: ignore


@lru_cache(maxsize=None)
def square_between(coord1: Coord, coord2: Coord) -> int:
    if coord1 > coord2:
        return square_between(coord2, coord1)
    return (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)


def print_grid(red_tiles: List[Coord], green_tiles: List[Coord]) -> None:
    all_tiles = set(red_tiles) | set(green_tiles)
    min_x = min(x for x, _ in all_tiles)
    max_x = max(x for x, _ in all_tiles)
    min_y = min(y for _, y in all_tiles)
    max_y = max(y for _, y in all_tiles)

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in green_tiles:
                row += "X"
            elif (x, y) in red_tiles:
                row += "#"
            else:
                row += "."
        print(row)


def part_A(input_filename: str) -> int:
    grid = read_input(input_filename)
    return max(square_between(pos_1, pos_2) for pos_1, pos_2 in product(grid, repeat=2))


def part_B(input_filename: str) -> int:
    red_tiles = read_input(input_filename)
    green_tiles = set()
    for first_tile, next_tile in pairwise(red_tiles + [red_tiles[0]]):
        x1, y1 = first_tile
        x2, y2 = next_tile
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x, y) not in red_tiles:
                    green_tiles.add((x, y))

    # print_grid(red_tiles, list(green_tiles))
    return 0


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
