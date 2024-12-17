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

from collections import defaultdict
from typing import Dict, List, Set, Tuple
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
        # Replace start and end with empty space
        maze[start_pos] = "."
        maze[end_pos] = "."
    return maze, start_pos, end_pos


def print_maze(maze: np.ndarray, best_place: Set[PositionYX], current_pos: PositionYX, orientation: str) -> None:
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if (y, x) == current_pos:
                print(orientation, end="")
            elif (y, x) in best_place:
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


def find_shortest_path(maze: np.ndarray, start: PositionYX, orientation: str, end: PositionYX) -> Tuple[int, str]:
    # Priority queue: (distance, position)
    queue: List[Tuple[int, Status, str]] = [(0, (start, orientation), "")]
    # Keep track of visited nodes and distances
    distances: Dict[Status, int] = {(start, orientation): 0}
    visited: Set[Status] = set()

    while queue:
        current_dist, (current_pos, current_orientation), path = heappop(queue)
        # print(f"Distance: {current_dist}")
        # print_maze(maze, path_cells, current_pos, current_orientation)

        if current_pos == end:
            return current_dist, path

        if (current_pos, current_orientation) in visited:
            continue

        visited.add((current_pos, current_orientation))

        for next_status, cost in get_next_position(current_pos, current_orientation, maze):
            distance = current_dist + cost
            if next_status not in distances or distance < distances[next_status]:
                distances[next_status] = distance
                heappush(queue, (distance, next_status, f"{path}{next_status[1]}"))

    return -1, ""


def part_A(input_filename: str) -> int:
    maze, start_pos, end_pos = read_input(input_filename)
    cost, path = find_shortest_path(maze, start_pos, "E", end_pos)
    # print_maze(maze)
    return cost


def find_all_shortest_paths(
    maze: np.ndarray, start: PositionYX, orientation: str, end: PositionYX
) -> List[Tuple[int, Set[PositionYX]]]:
    queue: List[Tuple[int, Status, Set[PositionYX]]] = [(0, (start, orientation), {start})]
    distances: Dict[Status, int] = {(start, orientation): 0}
    visited: Set[Status] = set()
    end_paths: Dict[int, List[Set[PositionYX]]] = defaultdict(list)  # distance -> paths

    while queue:
        current_dist, (current_pos, current_orientation), path_cells = heappop(queue)

        # Skip if we've seen better paths
        if (current_pos, current_orientation) in visited and distances[
            (current_pos, current_orientation)
        ] < current_dist:
            continue

        # If at end, record this path
        if current_pos == end:
            end_paths[current_dist].append(path_cells)
            # Don't stop - keep searching for other paths

        visited.add((current_pos, current_orientation))

        # Explore next positions
        for next_status, cost in get_next_position(current_pos, current_orientation, maze):
            next_dist = current_dist + cost
            next_pos = next_status[0]
            next_cells = path_cells.copy()
            next_cells.add(next_pos)

            if next_status not in distances or next_dist <= distances[next_status]:
                distances[next_status] = next_dist
                heappush(queue, (next_dist, next_status, next_cells))

    # Return all paths with minimum distance
    if not end_paths:
        return [(-1, set())]
    min_dist = min(end_paths.keys())
    return [(min_dist, cells) for cells in end_paths[min_dist]]


def part_B(input_filename: str) -> int:
    maze, start_pos, end_pos = read_input(input_filename)
    paths = find_all_shortest_paths(maze, start_pos, "E", end_pos)
    distinct_cells = set()
    for _, cells in paths:
        distinct_cells |= cells
    return len(distinct_cells)


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample1.txt"
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
