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
from typing import Generator, List, Tuple
from aoc_performance import aoc_perf

DAY = "13"
Array = List[List[str]]


def read_input(input_filename: str) -> List[Array]:
    with open(input_filename, "r") as input_file:
        input_data = input_file.read().split("\n\n")
        arrays = [[list(line) for line in a.split("\n")] for a in input_data]
    return arrays


def find_horizontal_symetry(array: Array, excep: int = 0) -> int:
    for index in range(len(array) - 1):
        symetry = True
        rows = 0
        while symetry and rows <= index and index + rows + 1 < len(array):
            symetry &= array[index - rows] == array[index + rows + 1]
            rows += 1
        if symetry and index + 1 != excep:
            return index + 1
    return 0


def rotate(array: Array) -> Array:
    return [[array[y][x] for y in range(len(array) - 1, -1, -1)] for x in range(len(array[0]))]


def find_vertical_symetry(array: Array, excep: int = 0) -> int:
    return find_horizontal_symetry(rotate(array), excep)


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
