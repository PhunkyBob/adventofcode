"""
Advent of Code 2024
--- Day 10: Hoof It ---
https://adventofcode.com/2024/day/10

This trailhead has a score of 2:

...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9

"""

from typing import Any, Callable, Dict, List, Set, Tuple
from collections import deque
from aoc_performance import aoc_perf

DAY = "10"
Array = List[List[int]]
Position = Tuple[int, int]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DISPLAY = {(-1, 0): "^", (1, 0): "v", (0, -1): "<", (0, 1): ">"}


def read_input(input_filename: str) -> Array:
    with open(input_filename, "r") as file:
        return [[int(char) if char != "." else -1 for char in line.strip()] for line in file]


def get_start_positions(data: Array) -> List[Position]:
    start_positions: List[Position] = [
        (row, col) for row in range(len(data)) for col in range(len(data[row])) if data[row][col] == 0
    ]
    return start_positions


def is_valid_position(data: Array, position: Position) -> bool:
    row, col = position
    return 0 <= row < len(data) and 0 <= col < len(data[row])


def print_data(data: Array, position: Position, direction: Position) -> None:
    for row, line in enumerate(data):
        for col, value in enumerate(line):
            if (row, col) == position:

                print(DISPLAY.get(direction, "X"), end="")
            else:
                print(value if value != -1 else ".", end="")
        print()
    print()


def count_destinations_from(data: Array, position: Position) -> Tuple[int, int]:
    destinations: Set[Position] = set()
    rating = 0
    if not is_valid_position(data, position):
        return 0, 0
    row, col = position
    if data[row][col] != 0:
        return 0, 0
    queue = deque([position])
    while queue:
        row, col = queue.popleft()
        for row_dir, col_dir in DIRECTIONS:
            new_row, new_col = row + row_dir, col + col_dir
            if not is_valid_position(data, (new_row, new_col)):
                continue
            if data[new_row][new_col] != data[row][col] + 1:
                continue
            if data[new_row][new_col] == 9:
                destinations.add((new_row, new_col))
                rating += 1
            else:
                queue.append((new_row, new_col))
    return len(destinations), rating


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    start_positions = get_start_positions(data)
    return sum(count_destinations_from(data, start)[0] for start in start_positions)


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    start_positions = get_start_positions(data)
    return sum(count_destinations_from(data, start)[1] for start in start_positions)


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample3.txt"
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
