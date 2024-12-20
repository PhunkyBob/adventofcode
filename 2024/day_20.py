"""
Advent of Code 2024
--- Day 20: Race Condition ---
https://adventofcode.com/2024/day/20

"""

from collections import Counter
from heapq import heappop, heappush
from typing import Dict, List, Set, Tuple
import numpy as np
from aoc_performance import aoc_perf

DAY = "20"

PositionYX = Tuple[int, int]
DIRECTIONS: Tuple[Tuple[int, int], ...] = ((0, -1), (1, 0), (0, 1), (-1, 0))


def read_input(input_filename: str) -> Tuple[np.ndarray, PositionYX, PositionYX]:
    with open(input_filename, "r") as file:
        maze = np.array([list(line.strip()) for line in file.readlines()])
        start_pos = tuple(np.argwhere(maze == "S")[0])
        end_pos = tuple(np.argwhere(maze == "E")[0])
        # Replace start and end with empty space
        maze[start_pos] = "."
        maze[end_pos] = "."
    return maze, start_pos, end_pos


def print_maze(maze: np.ndarray, current_pos: PositionYX, path: Set[PositionYX]) -> None:
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if (y, x) == current_pos:
                print("@", end="")
            elif (y, x) in path:
                print("O", end="")
            else:
                print(cell, end="")
        print()


def find_shortest_path(maze: np.ndarray, start: PositionYX, end: PositionYX) -> Tuple[int, Dict[PositionYX, int]]:
    # Priority queue: (distance, position)
    queue: List[Tuple[int, PositionYX, Set[PositionYX]]] = [(0, start, {start})]
    # Keep track of visited nodes and distances
    distances: Dict[PositionYX, int] = {start: 0}
    visited: Set[PositionYX] = set()

    while queue:
        current_dist, current_pos, path = heappop(queue)
        # print(f"Distance: {current_dist}")
        # print_maze(maze, path_cells, current_pos, current_orientation)

        if current_pos == end:
            complete_path = {pos: distances[pos] for pos in path}
            return current_dist, complete_path

        if current_pos in visited:
            continue

        visited.add(current_pos)

        for direction in DIRECTIONS:
            next_position = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if maze[next_position] == "#":
                continue
            distance = current_dist + 1
            if next_position not in distances or distance < distances[next_position]:
                distances[next_position] = distance
                heappush(queue, (distance, next_position, path | {next_position}))

    return -1, {}


def manhattan_distance(pos1: PositionYX, pos2: PositionYX) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def list_shortcuts(path: Dict[PositionYX, int], distance: int = 2) -> Dict[int, int]:
    saves = Counter()
    already_checked = set()
    for cell in path:
        y, x = cell
        for i in range(-distance, distance + 1):
            for j in range(-distance + abs(i), distance - abs(i) + 1):
                new_cell = (y + i, x + j)
                if new_cell not in already_checked and new_cell in path:
                    man_dist = manhattan_distance(cell, new_cell)
                    saved_distance = int(abs(path[cell] - path[new_cell]) - man_dist)
                    saves[saved_distance] += 1
        already_checked.add(cell)
    return saves


def part_A(input_filename: str, save_at_least: int) -> int:
    maze, start_pos, end_pos = read_input(input_filename)
    distance, path = find_shortest_path(maze, start_pos, end_pos)
    # print_maze(maze, start_pos, set(path.keys()))
    shortcuts = list_shortcuts(path)
    # print(shortcuts)
    return sum(v for k, v in shortcuts.items() if k >= save_at_least)


def part_B(input_filename: str, save_at_least) -> int:
    maze, start_pos, end_pos = read_input(input_filename)
    distance, path = find_shortest_path(maze, start_pos, end_pos)
    # print_maze(maze, start_pos, set(path.keys()))
    shortcuts = list_shortcuts(path, 20)
    # print(shortcuts)
    return sum(v for k, v in shortcuts.items() if k >= save_at_least)


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    save_at_least_A = 1
    save_at_least_B = 50
    input_filename = f"day_{DAY}_input.txt"
    save_at_least_A = 100
    save_at_least_B = 100

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename, save_at_least_A)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename, save_at_least_B)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
