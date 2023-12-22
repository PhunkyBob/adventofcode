"""
Advent of Code 2023
--- Day 13: Point of Incidence ---
https://adventofcode.com/2023/day/13

For example:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.
"""

import itertools
from typing import Generator, List, Tuple
from aoc_performance import aoc_perf

DAY = "13"
Array = List[List[str]]


def read_input(input_filename: str) -> List[Array]:
    with open(input_filename, "r") as input_file:
        input_data = input_file.read().split("\n\n")
        arrays = [[list(line) for line in a.split("\n")] for a in input_data]
    return arrays


def rotate(array: Array) -> Array:
    """Rotate a matrix 90 degrees clockwise."""
    return [[array[y][x] for y in range(len(array) - 1, -1, -1)] for x in range(len(array[0]))]


def find_horizontal_symetry(array: Array, excep: int = 0) -> int:
    for index in range(len(array) - 1):
        if index + 1 == excep:
            continue

        symetry = True
        rows = 0
        while symetry and rows <= index and index + rows + 1 < len(array):
            symetry &= array[index - rows] == array[index + rows + 1]
            rows += 1
        if symetry:
            return index + 1
    return 0


def find_vertical_symetry(array: Array, excep: int = 0) -> int:
    return find_horizontal_symetry(rotate(array), excep)


def count_differences(array1: Array, array2: Array) -> int:
    """Count the number of differences between two matrix."""
    return sum(array1[y][x] != array2[y][x] for y, x in itertools.product(range(len(array1)), range(len(array1[0]))))


def find_horizontal_symetry_block(array: Array, allowed_diff: int = 0, excep: int = 0) -> int:
    for index in range(len(array) - 1):
        if index + 1 == excep:
            continue
        width = min(index + 1, len(array) - index - 1)
        slice_top_reversed = array[index + 1 - width : index + 1][::-1]
        slice_below = array[index + 1 : index + 1 + width]
        if count_differences(slice_top_reversed, slice_below) <= allowed_diff:
            return index + 1

    return 0


def find_vertical_symetry_block(array: Array, allowed_diff: int = 0, excep: int = 0) -> int:
    return find_horizontal_symetry_block(rotate(array), allowed_diff, excep)


def modified_array_generator(array: Array) -> Generator[Array, None, None]:
    for y in range(len(array)):
        for x in range(len(array[0])):
            new_array = [row[:] for row in array]
            new_array[y][x] = "#" if new_array[y][x] == "." else "."
            yield new_array


def part_A(input_filename: str) -> int:
    arrays = read_input(input_filename)
    total_left = 0
    total_top = 0
    for array in arrays:
        if symetry := find_horizontal_symetry(array):
            total_top += symetry
            continue
        if symetry := find_vertical_symetry(array):
            total_left += symetry
    return total_left + total_top * 100


def part_B(input_filename: str) -> int:
    arrays = read_input(input_filename)
    total_left = 0
    total_above = 0

    for array in arrays:
        original_above = find_horizontal_symetry(array)
        original_left = find_vertical_symetry(array)
        if symetry := find_horizontal_symetry_block(array, 1, original_above):
            total_above += symetry
        if symetry := find_vertical_symetry_block(array, 1, original_left):
            total_left += symetry
    return total_left + total_above * 100


def part_B_old(input_filename: str) -> int:
    arrays = read_input(input_filename)
    total_left = 0
    total_above = 0

    for array in arrays:
        original_above = find_horizontal_symetry(array)
        original_left = find_vertical_symetry(array)
        for modified_array in modified_array_generator(array):
            if symetry := find_horizontal_symetry(modified_array, original_above):
                if symetry != original_above:
                    total_above += symetry
                    break
            if symetry := find_vertical_symetry(modified_array, original_left):
                if symetry != original_left:
                    total_left += symetry
                    break
    return total_left + total_above * 100


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
