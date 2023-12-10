"""
Advent of Code 2023

https://adventofcode.com/2023/day/10

"""
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, List, Dict, Set, Tuple
from aoc_performance import aoc_perf

DAY = "10"


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


better_display = {"F": "┌", "L": "└", "7": "┐", "J": "┘", "|": "│", "-": "─", "S": "┼", ".": " "}


def get_next_position(direction: Direction, start_position: Tuple[int, int] = (0, 0)) -> Tuple[int, int]:
    if direction == Direction.NORTH:
        return (start_position[0] - 1, start_position[1])
    elif direction == Direction.EAST:
        return (start_position[0], start_position[1] + 1)
    elif direction == Direction.SOUTH:
        return (start_position[0] + 1, start_position[1])
    elif direction == Direction.WEST:
        return (start_position[0], start_position[1] - 1)
    else:
        raise ValueError(f"Unknown direction: {direction}")


def get_opposite_direction(direction: Direction) -> Direction:
    return Direction((direction.value + 2) % 4)


def pipe_to_directions(pipe: str) -> Set[Direction]:
    if pipe == "|":
        return {Direction.NORTH, Direction.SOUTH}
    elif pipe == "-":
        return {Direction.EAST, Direction.WEST}
    elif pipe == "L":
        return {Direction.NORTH, Direction.EAST}
    elif pipe == "J":
        return {Direction.NORTH, Direction.WEST}
    elif pipe == "7":
        return {Direction.SOUTH, Direction.WEST}
    elif pipe == "F":
        return {Direction.SOUTH, Direction.EAST}
    elif pipe == ".":
        return set()
    elif pipe == "S":
        return {Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST}
    else:
        raise ValueError(f"Unknown pipe: {pipe}")


class Pipe:
    connections: Set[Direction]
    is_starting_pipe: bool
    original_char: str

    def __init__(self, pipe: str) -> None:
        self.connections = pipe_to_directions(pipe)
        self.is_starting_pipe = pipe == "S"
        self.original_char = pipe

    def is_connected(self, other: "Pipe", direction: Direction) -> bool:
        return direction in self.connections and get_opposite_direction(direction) in other.connections


Map = List[List[Pipe]]


def read_input(input_filename: str) -> Map:
    with open(input_filename, "r") as input_file:
        return [[Pipe(pipe) for pipe in line.strip()] for line in input_file]


def get_starting_pipes(data: Map) -> Tuple[int, int]:
    for row_index, row in enumerate(data):
        for col_index, pipe in enumerate(row):
            if pipe.is_starting_pipe:
                return (row_index, col_index)
    raise ValueError("No starting pipe found")


def clean_start(data: Map, starting_row: int, starting_col: int) -> Map:
    """This removes the 2 unnecessary connections from the starting pipe."""
    connected_directions: Set[Direction] = set()
    for direction in [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]:
        test_row, test_col = get_next_position(direction, (starting_row, starting_col))
        if data[starting_row][starting_col].is_connected(data[test_row][test_col], direction):
            connected_directions.add(direction)
    data[starting_row][starting_col].connections = connected_directions
    return data


def get_steps(data: Map, starting_row: int, starting_col: int) -> Set[Tuple[int, int]]:
    """Returns a list of steps (row, col) to loop in the map from starting postion."""
    start_direction = next(iter(data[starting_row][starting_col].connections))
    steps: Set[Tuple[int, int]] = {(starting_row, starting_col)}
    current_row, current_col = get_next_position(start_direction, (starting_row, starting_col))
    current_direction = start_direction
    while (current_row, current_col) != (starting_row, starting_col):
        current_pipe = data[current_row][current_col]
        for direction in current_pipe.connections:
            if direction != get_opposite_direction(current_direction):
                current_direction = direction
                break
        steps.add((current_row, current_col))
        current_row, current_col = get_next_position(current_direction, (current_row, current_col))
    return steps


def count_inside(data: Map, steps: Set[Tuple[int, int]]) -> int:
    def is_inside(row: int, col: int) -> bool:
        i = row - 1
        count_west = 0
        count_east = 0
        while i >= 0:
            # if (i, col) in memory:
            #     count_west += memory[(i, col)][0]
            #     count_east += memory[(i, col)][1]
            #     break
            if memory[i][col]:
                count_west += memory[i][col][0]
                count_east += memory[i][col][1]
                break
            if (i, col) in steps:
                count_west += 1 if Direction.WEST in data[i][col].connections else 0
                count_east += 1 if Direction.EAST in data[i][col].connections else 0
            i -= 1
        memory[row][col] = (count_west, count_east)
        return min(count_west, count_east) % 2 == 1

    memory = [[None for _ in row] for row in data]
    # memory = {}
    total_inside = 0
    for row_index, row in enumerate(data):
        for col_index, pipe in enumerate(row):
            if (row_index, col_index) not in steps and is_inside(row_index, col_index):
                total_inside += 1
            # print(".", end="", flush=True)
        # print()
    return total_inside


def print_map(data: Map, steps: Set[Tuple[int, int]]) -> None:
    for row_index, row in enumerate(data):
        for col_index, pipe in enumerate(row):
            if (row_index, col_index) in steps:
                print(better_display[pipe.original_char], end="")
            else:
                print(".", end="")
        print()


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    starting_row, starting_col = get_starting_pipes(data)
    data = clean_start(data, starting_row, starting_col)
    steps = get_steps(data, starting_row, starting_col)
    # print_map(data, steps)
    return len(steps) // 2


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    starting_row, starting_col = get_starting_pipes(data)
    data = clean_start(data, starting_row, starting_col)
    steps = get_steps(data, starting_row, starting_col)
    return count_inside(data, steps)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample5.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected: 6942

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected: 297


if __name__ == "__main__":
    main()
