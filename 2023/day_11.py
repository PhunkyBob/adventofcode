"""
Advent of Code 2023
--- Day 11: Cosmic Expansion ---
https://adventofcode.com/2023/day/11

The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies.

"""
from typing import Any, Callable, List, Dict, NamedTuple, Set
from aoc_performance import aoc_perf
from itertools import combinations_with_replacement

DAY = "11"


class Coordinate(NamedTuple):
    col: int
    row: int


def read_input(input_filename: str) -> Set[Coordinate]:
    with open(input_filename, "r") as input_file:
        coordinates = {
            Coordinate(col, row) for row, line in enumerate(input_file) for col, char in enumerate(line) if char == "#"
        }
    return coordinates


def expand_universe(universe: Set[Coordinate], multiply_size=2) -> Set[Coordinate]:
    new_universe = set()
    max_col = max(coordinate.col for coordinate in universe)
    max_row = max(coordinate.row for coordinate in universe)
    empty_cols = {col for col in range(max_col + 1) if all(coordinate.col != col for coordinate in universe)}
    empty_rows = {row for row in range(max_row + 1) if all(coordinate.row != row for coordinate in universe)}
    for coordinate in universe:
        empty_cols_before = sum(col < coordinate.col for col in empty_cols)
        empty_rows_before = sum(row < coordinate.row for row in empty_rows)
        new_universe.add(
            Coordinate(
                coordinate.col + empty_cols_before * (multiply_size - 1),
                coordinate.row + empty_rows_before * (multiply_size - 1),
            )
        )
    return new_universe


def get_manhattan_distance(coord1: Coordinate, coord2: Coordinate) -> int:
    return abs(coord1.col - coord2.col) + abs(coord1.row - coord2.row)


def part_A(input_filename: str) -> int:
    universe = read_input(input_filename)
    expanded_universe = expand_universe(universe)
    return sum(
        get_manhattan_distance(coord1, coord2)
        for coord1, coord2 in combinations_with_replacement(expanded_universe, 2)
    )


def part_B(input_filename: str) -> int:
    universe = read_input(input_filename)
    expanded_universe = expand_universe(universe, 1000000)
    return sum(
        get_manhattan_distance(coord1, coord2)
        for coord1, coord2 in combinations_with_replacement(expanded_universe, 2)
    )


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

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
