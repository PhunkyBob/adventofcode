"""
Advent of Code 2024
--- Day 20: Race Condition ---
https://adventofcode.com/2024/day/20

"""

from heapq import heappop, heappush
import math
from typing import Any, Callable, Dict, List, Set, Tuple
import numpy as np
from aoc_performance import aoc_perf

DAY = "20"

PositionYX = Tuple[int, int]
DIRECTIONS: Set[Tuple[int, int]] = {(0, -1), (1, 0), (0, 1), (-1, 0)}  # N, E, S, W


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


def list_shortcuts(maze: np.ndarray, path: Dict[PositionYX, int]) -> Dict[int, int]:
    saves: Dict[int, int] = {}
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell != "#":
                continue
            min_distance = math.inf
            max_distance = 0
            items_around = 0
            for direction in DIRECTIONS:
                next_position = (y + direction[0], x + direction[1])
                if next_position in path:
                    items_around += 1
                    distance = path[next_position]
                    if distance > max_distance:
                        max_distance = distance
                    if distance < min_distance:
                        min_distance = distance
            if items_around >= 2:
                saves[int(max_distance - min_distance - 2)] = saves.get(int(max_distance - min_distance - 2), 0) + 1
    return saves


def part_A(input_filename: str) -> int:
    maze, start_pos, end_pos = read_input(input_filename)
    distance, path = find_shortest_path(maze, start_pos, end_pos)
    # print_maze(maze, start_pos, set(path.keys()))
    shortcuts = list_shortcuts(maze, path)
    # print(shortcuts)
    return sum(v for k, v in shortcuts.items() if k >= 100)


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
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
