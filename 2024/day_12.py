"""
Advent of Code 2024
--- Day 12: Garden Groups ---
https://adventofcode.com/2024/day/12

+-+-+-+-+
|A A A A|
+-+-+-+-+     +-+
              |D|
+-+-+   +-+   +-+
|B B|   |C|
+   +   + +-+
|B B|   |C C|
+-+-+   +-+ +
          |C|
+-+-+-+   +-+
|E E E|
+-+-+-+
"""

from typing import Any, Callable, Dict, List, Set, Tuple
import polars as pl
from collections import deque

from aoc_performance import aoc_perf

DAY = "12"

Position = Tuple[int, int]
DIRECTIONS: Dict[str, Position] = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}


def read_input(input_filename: str) -> pl.DataFrame:
    with open(input_filename, "r") as file:
        matrix = [list(line.strip()) for line in file]
        df = pl.DataFrame(matrix)
    return df


def get_full_region(matrix: pl.DataFrame, from_x: int, from_y: int) -> Set[Position]:
    region: Set[Position] = {(from_x, from_y)}
    search_value = matrix[from_x, from_y]
    to_visit = deque([(from_x, from_y)])
    while to_visit:
        x, y = to_visit.pop()
        region.add((x, y))
        for dx, dy in DIRECTIONS.values():
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < matrix.shape[0]
                and 0 <= new_y < matrix.shape[1]
                and matrix[new_x, new_y] == search_value
                and (new_x, new_y) not in region
            ):
                to_visit.append((new_x, new_y))
    return region


def get_region_perimeter(region: Set[Position]) -> int:
    perimeter = 0
    for garden in region:
        x, y = garden
        for dx, dy in DIRECTIONS.values():
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in region:
                perimeter += 1
    return perimeter


def get_region_sides(region: Set[Position]) -> int:
    perimeter = 0
    for garden in region:
        x, y = garden
        for dir, (dx, dy) in DIRECTIONS.items():
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in region:
                discount = False
                if dir == "W" and (x, y - 1) in region and (x - 1, y - 1) not in region:
                    discount = True
                elif dir == "N" and (x + 1, y) in region and (x + 1, y - 1) not in region:
                    discount = True
                elif dir == "E" and (x, y + 1) in region and (x + 1, y + 1) not in region:
                    discount = True
                elif dir == "S" and (x - 1, y) in region and (x - 1, y + 1) not in region:
                    discount = True

                if not discount:
                    perimeter += 1
    return perimeter


def get_region_price(region: Set[Position]) -> int:
    return len(region) * get_region_perimeter(region)


def get_region_discount_price(region: Set[Position]) -> int:
    return len(region) * get_region_sides(region)


def get_all_regions(matrix) -> Dict[int, Set[Position]]:
    all_regions: Dict[int, Set[Position]] = {}
    all_explored: Set[Position] = set()
    region_id = 0
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if (x, y) not in all_explored:
                region = get_full_region(matrix, x, y)
                all_explored.update(region)
                all_regions[region_id] = region
                region_id += 1
    return all_regions


def part_A(input_filename: str) -> int:
    matrix = read_input(input_filename)
    all_regions: Dict[int, Set[Position]] = get_all_regions(matrix)
    return sum(get_region_price(region) for region in all_regions.values())


def part_B(input_filename: str) -> int:
    matrix = read_input(input_filename)
    all_regions: Dict[int, Set[Position]] = get_all_regions(matrix)
    return sum(get_region_discount_price(region) for region in all_regions.values())


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample2.txt"
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
