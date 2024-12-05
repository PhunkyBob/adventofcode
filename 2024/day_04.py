"""
Advent of Code 2024
--- Day 4: Ceres Search ---
https://adventofcode.com/2024/day/4

..X...
.SAMX.
.A..A.
XMAS.S
.X....

Count XMAS in the matrix.
"""

from typing import List

from aoc_performance import aoc_perf

DAY = "04"

DIRECTIONS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
    "NE": (1, 1),
    "NW": (-1, 1),
    "SE": (1, -1),
    "SW": (-1, -1),
}


def read_input(input_filename: str) -> List[List[str]]:
    with open(input_filename, "r") as file:
        return [list(line.strip()) for line in file]


def is_out_of_bounds(matrix: List[List[str]], x: int, y: int) -> bool:
    return x < 0 or y < 0 or y >= len(matrix) or x >= len(matrix[y])


def count_xmas_from(matrix: List[List[str]], start_x: int, start_y: int) -> int:
    if matrix[start_y][start_x] != "X":
        return 0

    xmas_count = 0
    expected = ["M", "A", "S"]

    for dx, dy in DIRECTIONS.values():
        x, y = start_x, start_y
        for char in expected:
            x += dx
            y += dy
            if is_out_of_bounds(matrix, x, y) or matrix[y][x] != char:
                break
        else:
            xmas_count += 1

    return xmas_count


def part_A(input_filename: str) -> int:
    matrix = read_input(input_filename)
    return sum(
        count_xmas_from(matrix, x, y) for y in range(len(matrix)) for x in range(len(matrix[y])) if matrix[y][x] == "X"
    )


def count_mas_in_x_from(matrix: List[List[str]], start_x: int, start_y: int) -> int:
    xmas_count = 0
    if is_out_of_bounds(matrix, start_x, start_y):
        return 0
    x = start_x
    y = start_y
    if matrix[y][x] != "A":
        return 0

    diagonal_words_accepted = {("M", "A", "S"), ("S", "A", "M")}
    diagonal_up_word = (matrix[y - 1][x - 1], "A", matrix[y + 1][x + 1])
    if diagonal_up_word in diagonal_words_accepted:
        diagonal_down_word = (matrix[y + 1][x - 1], "A", matrix[y - 1][x + 1])
        if diagonal_down_word in diagonal_words_accepted:
            xmas_count += 1
    return xmas_count


def part_B(input_filename: str) -> int:
    matrix = read_input(input_filename)
    return sum(
        count_mas_in_x_from(matrix, x, y)
        for y in range(1, len(matrix) - 1)
        for x in range(1, len(matrix[y]) - 1)
        if matrix[y][x] == "A"
    )


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

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
