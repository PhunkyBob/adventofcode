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
import numpy as np

from collections import deque

from aoc_performance import aoc_perf

DAY = "12"

Position = Tuple[int, int]
DIRECTIONS: Dict[str, Position] = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}


def read_input(input_filename: str) -> np.ndarray:
    return np.array([list(line.strip()) for line in open(input_filename)])


def get_full_region(matrix: np.ndarray, from_x: int, from_y: int) -> Set[Position]:
    region = set()
    search_value = matrix[from_x, from_y]
    to_visit = [(from_x, from_y)]
    while to_visit:
        x, y = to_visit.pop()
        if (x, y) in region:
            continue
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


def calculate_regions_and_prices(matrix: np.ndarray, use_discount: bool = False):
    total_price = 0
    explored = np.zeros_like(matrix, dtype=bool)

    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if not explored[x, y]:
                region = get_full_region(matrix, x, y)

                # Mark explored
                for rx, ry in region:
                    explored[rx, ry] = True

                # Calculate price
                if use_discount:
                    price = calculate_discounted_region_price(region)
                else:
                    price = calculate_standard_region_price(region)

                total_price += price

    return total_price


def calculate_standard_region_price(region: Set[Position]) -> int:
    return len(region) * count_region_perimeter(region)


def calculate_discounted_region_price(region: Set[Position]) -> int:
    return len(region) * count_region_sides(region)


def count_region_perimeter(region: Set[Position]) -> int:
    perimeter = 0
    for x, y in region:
        for dx, dy in DIRECTIONS.values():
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in region:
                perimeter += 1
    return perimeter


def count_region_sides(region: Set[Position]) -> int:
    perimeter = 0
    for x, y in region:
        for direction, (dx, dy) in DIRECTIONS.items():
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in region and not is_side_discounted(region, x, y, direction):
                perimeter += 1
    return perimeter


def is_side_discounted(region: Set[Position], x: int, y: int, direction: str) -> bool:
    discounts = {
        "N": ((x + 1, y) in region and (x + 1, y - 1) not in region),
        "E": ((x, y + 1) in region and (x + 1, y + 1) not in region),
        "S": ((x - 1, y) in region and (x - 1, y + 1) not in region),
        "W": ((x, y - 1) in region and (x - 1, y - 1) not in region),
    }
    return discounts[direction]


def part_A(input_filename: str) -> int:
    matrix = read_input(input_filename)
    return calculate_regions_and_prices(matrix, use_discount=False)


def part_B(input_filename: str) -> int:
    matrix = read_input(input_filename)
    return calculate_regions_and_prices(matrix, use_discount=True)


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
