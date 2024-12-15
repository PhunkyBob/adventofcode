"""
Advent of Code 2024
--- Day 15: Warehouse Woes ---
https://adventofcode.com/2024/day/15

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

As the robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those boxes.
"""

import itertools
from typing import Any, Callable, Dict, List, Tuple

from aoc_performance import aoc_perf
import numpy as np

DAY = "15"

Position = Tuple[int, int]
DIRECTIONS: Dict[str, Position] = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}


def read_input(input_filename: str) -> Tuple[np.ndarray, str, Position]:
    with open(input_filename, "r") as file:
        warehouse, moves = file.read().split("\n\n")
        warehouse_array = np.array([list(line) for line in warehouse.strip().split("\n")])
        for y, x in np.argwhere(warehouse_array == "@"):
            robot_position = (x, y)
        warehouse_array[robot_position[1], robot_position[0]] = "."
        return warehouse_array, moves.replace("\n", ""), robot_position


def move_direction(warehouse: np.ndarray, position: Position, move: str) -> bool:
    dx, dy = DIRECTIONS[move]
    new_x, new_y = position[0] + dx, position[1] + dy
    while warehouse[new_y, new_x] == "O":
        new_x, new_y = new_x + dx, new_y + dy
    if warehouse[new_y, new_x] == ".":
        warehouse[new_y, new_x] = "O"
        warehouse[position[1], position[0]] = "."
        return True
    return False


def print_warehouse(warehouse: np.ndarray, robot_position: Position, move: str) -> None:
    print(f"Move: {move}")
    for y in range(warehouse.shape[0]):
        for x in range(warehouse.shape[1]):
            if (x, y) == robot_position:
                print("@", end="")
            else:
                print(warehouse[y, x], end="")
        print()


def get_sum_of_gps_coordinates(warehouse: np.ndarray) -> int:
    return sum(
        x + y * 100
        for y, x in itertools.product(range(warehouse.shape[0]), range(warehouse.shape[1]))
        if warehouse[y, x] == "O"
    )


def part_A(input_filename: str) -> int:
    warehouse, moves, robot_position = read_input(input_filename)
    # print_warehouse(warehouse, robot_position, "Start")
    for move in moves:
        dx, dy = DIRECTIONS[move]
        new_x, new_y = robot_position[0] + dx, robot_position[1] + dy
        if warehouse[new_y, new_x] == "O" and move_direction(warehouse, (new_x, new_y), move):
            robot_position = new_x, new_y
        elif warehouse[new_y, new_x] == ".":
            robot_position = new_x, new_y
        # print_warehouse(warehouse, robot_position, move)

    return get_sum_of_gps_coordinates(warehouse)


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample2.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
