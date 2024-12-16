"""
Advent of Code 2024
--- Day 16: Reindeer Maze ---
https://adventofcode.com/2024/day/16

###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############

The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).
"""

from typing import Any, Callable, Dict, List, Set, Tuple
from heapq import heappush, heappop

import numpy as np

from aoc_performance import aoc_perf

DAY = "16"
DIRECTIONS: Dict[str, Tuple[int, int]] = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
POSSIBLE_DIRECTIONS_FROM: Dict[str, List[str]] = {"N": ["W", "E"], "E": ["N", "S"], "S": ["E", "W"], "W": ["S", "N"]}
PositionYX = Tuple[int, int]
Status = Tuple[PositionYX, str]  # (Position, Orientation)


def read_input(input_filename: str) -> Tuple[np.ndarray, PositionYX, PositionYX]:
    with open(input_filename, "r") as file:
        maze = np.array([list(line.strip()) for line in file.readlines()])
        start_pos = tuple(np.argwhere(maze == "S")[0])
        end_pos = tuple(np.argwhere(maze == "E")[0])
        maze[start_pos] = "."
        maze[end_pos] = "."
    return maze, start_pos, end_pos


def print_maze(maze: np.ndarray, best_place: Set[PositionYX]) -> None:
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if (y, x) in best_place:
                print("O", end="")
            else:
                print(cell, end="")
        print()
    # for row in maze:
    #     print("".join(row))


def get_next_position(pos: PositionYX, direction: str, maze: np.ndarray) -> List[Tuple[Status, int]]:
    y, x = pos
    neighbors = []
    dx, dy = DIRECTIONS[direction]
    new_x, new_y = x + dx, y + dy
    status = ((new_y, new_x), direction)
    if 0 <= new_x < maze.shape[1] and 0 <= new_y < maze.shape[0] and maze[new_y, new_x] == ".":
        neighbors.append((status, 1))
    for new_direction in POSSIBLE_DIRECTIONS_FROM[direction]:
        status = ((y, x), new_direction)
        neighbors.append((status, 1000))
    return neighbors


def find_shortest_path(maze: np.ndarray, start: PositionYX, orientation: str, end: PositionYX) -> int:
    # Priority queue: (distance, position)
    best_place: Set[PositionYX] = set()
    queue: List[Tuple[int, Status, str, Set[PositionYX]]] = [(0, (start, orientation), "", best_place)]
    # Keep track of visited nodes and distances
    distances: Dict[Status, int] = {(start, orientation): 0}
    visited: Set[Status] = set()

    while queue:
        current_dist, (current_pos, current_orientation), path, best_place = heappop(queue)

        if current_pos == end:
            print(f"Path: {path} (length: {len(path)})")
            print(f"Best place: {best_place} (length: {len(best_place)})")
            print_maze(maze, best_place)
            return current_dist

        if (current_pos, current_orientation) in visited:
            continue

        visited.add((current_pos, current_orientation))

        for next_status, cost in get_next_position(current_pos, current_orientation, maze):
            distance = current_dist + cost
            if next_status not in distances or distance < distances[next_status]:
                distances[next_status] = distance
                heappush(queue, (distance, next_status, f"{path}{next_status[1]}", best_place | {current_pos}))

    return -1  # No path found


def part_A(input_filename: str) -> int:
    maze, start_pos, end_pos = read_input(input_filename)
    cost = find_shortest_path(maze, start_pos, "E", end_pos)
    # print_maze(maze)
    return cost


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input_sample1.txt"
    # input_filename = f"day_{DAY}_input.txt"

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
