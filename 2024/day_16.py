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
Position = Tuple[int, int]
Status = Tuple[Position, str]  # (Position, Orientation)


def read_input(input_filename: str) -> Tuple[np.ndarray, Position, Position]:
    with open(input_filename, "r") as file:
        maze = np.array([list(line.strip()) for line in file.readlines()])
        start_pos = tuple(np.argwhere(maze == "S")[0])
        end_pos = tuple(np.argwhere(maze == "E")[0])
        maze[start_pos[1], start_pos[0]] = "."
        maze[end_pos[1], end_pos[0]] = "."
    return maze, start_pos, end_pos


def print_maze(maze: np.ndarray) -> None:
    for row in maze:
        print("".join(row))


def get_next_position(pos: Position, direction: str, maze: np.ndarray) -> List[Tuple[Status, int]]:
    x, y = pos
    neighbors = []
    dx, dy = DIRECTIONS[direction]
    new_x, new_y = x + dx, y + dy
    status = ((new_x, new_y), direction)
    if 0 <= new_x < maze.shape[1] and 0 <= new_y < maze.shape[0] and maze[new_y, new_x] == ".":
        neighbors.append((status, 1))
    for new_direction in POSSIBLE_DIRECTIONS_FROM[direction]:
        status = ((x, y), new_direction)
        neighbors.append((status, 1000))
    return neighbors


def find_shortest_path(maze: np.ndarray, start: Position, orientation: str, end: Position) -> int:
    # Priority queue: (distance, position)
    queue: List[Tuple[int, Status]] = [(0, (start, orientation))]
    # Keep track of visited nodes and distances
    distances: Dict[Status, int] = {(start, orientation): 0}
    visited: Set[Status] = set()

    while queue:
        current_dist, (current_pos, current_orientation) = heappop(queue)

        if current_pos == end:
            return current_dist

        if (current_pos, current_orientation) in visited:
            continue

        visited.add((current_pos, current_orientation))

        for next_status, cost in get_next_position(current_pos, current_orientation, maze):
            distance = current_dist + cost
            if next_status not in distances or distance < distances[next_status]:
                distances[next_status] = distance
                heappush(queue, (distance, next_status))

    return -1  # No path found


def part_A(input_filename: str) -> int:
    maze, start_pos, end_pos = read_input(input_filename)
    cost = find_shortest_path(maze, start_pos, "E", end_pos)
    # print_maze(maze)
    return cost


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input_sample2.txt"
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
