"""
Advent of Code 2024
--- Day 18: RAM Run ---
https://adventofcode.com/2024/day/18

OO.#OOO
.O#OO#O
.OOO#OO
...#OO#
..#OO#.
.#.O#..
#.#OOOO

"""

from heapq import heappop, heappush
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

import numpy as np

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "18"

Position = Tuple[int, int]
DIRECTIONS: Dict[str, Tuple[int, int]] = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def read_input(input_filename: str) -> List[Position]:
    memory_space = []
    with open(input_filename, "r") as file:
        for line in file.readlines():
            x, y = line.split(",")
            memory_space.append((int(x), int(y)))
    return memory_space


def print_memory_space(
    memory_space: List[Position], width: int, steps: int = -1, visited: Optional[Set[Position]] = None
) -> None:
    visited = visited or set()
    memory_at_step = set(memory_space[:steps])

    for y in range(width):
        for x in range(width):
            if (x, y) in memory_at_step:
                print("#", end="")
            elif (x, y) in visited:
                print("O", end="")
            else:
                print(".", end="")
        print()


def find_shortest_path(memory_space: Set[Position], start: Position, end: Position, width: int) -> Tuple[int, Set]:
    # Priority queue: (distance, position)
    path = {start}
    queue: List[Tuple[int, Position, Set[Position]]] = [(0, start, path)]
    # Keep track of visited nodes and distances
    distances: Dict[Position, int] = {start: 0}
    visited: Set[Position] = set()

    while queue:
        current_dist, current_pos, path = heappop(queue)
        # print(f"Distance: {current_dist}")

        if current_pos == end:
            # print_memory_space(memory_space, width, len(memory_space), path)
            return current_dist, path

        if current_pos in visited:
            continue

        visited.add(current_pos)

        for next_direction in DIRECTIONS.values():
            new_x, new_y = current_pos[0] + next_direction[0], current_pos[1] + next_direction[1]
            next_position = (new_x, new_y)
            if next_position in memory_space or new_x < 0 or new_x >= width or new_y < 0 or new_y >= width:
                continue
            distance = current_dist + 1
            if next_position not in distances or distance < distances[next_position]:
                distances[next_position] = distance
                new_path = path.copy()
                new_path.add(next_position)
                heappush(queue, (distance, next_position, new_path))

    return -1, set()


def part_A(input_filename: str, width: int, already_fallen: int) -> int:
    memory_space = read_input(input_filename)
    start_pos = (0, 0)
    end_pos = (width - 1, width - 1)
    cost, path = find_shortest_path(set(memory_space[:already_fallen]), start_pos, end_pos, width)
    # print_memory_space(memory_space, width, already_fallen, path)
    return cost


def part_B(input_filename: str, width: int, already_fallen: int) -> str:
    memory_space = read_input(input_filename)
    start_pos = (0, 0)
    end_pos = (width - 1, width - 1)
    # Fisrt shot: we know it's a valid path.
    cost, path = find_shortest_path(set(memory_space[:already_fallen]), start_pos, end_pos, width)
    for part in range(already_fallen, len(memory_space)):
        if memory_space[part] not in path:
            # The is not in the way, no need to check
            continue
        cost, path = find_shortest_path(set(memory_space[: part + 1]), start_pos, end_pos, width)
        # print_memory_space(memory_space, width, part, path)
        if cost < 0:
            obstacle = memory_space[part]
            return f"{obstacle[0]},{obstacle[1]}"
    return ""


def main() -> None:
    download_input(DAY, 2024)
    # input_filename = f"day_{DAY}_input_sample.txt"
    # width = 7
    # already_fallen = 12
    input_filename = f"day_{DAY}_input.txt"
    width = 71
    already_fallen = 1024

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename, width, already_fallen)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename, width, already_fallen)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
