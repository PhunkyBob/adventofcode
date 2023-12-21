"""
Advent of Code 2023

https://adventofcode.com/2023/day/17

"""
from enum import Enum
from typing import Any, Callable, List, Dict, NamedTuple, Optional, Tuple
from aoc_performance import aoc_perf
import heapq

DAY = "17"


# class Direction(Enum):
Direction = Tuple[int, int]
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


# class Coord(NamedTuple):
#     x: int
#     y: int

#     def __add__(self, direction: Direction) -> "Coord":
#         return Coord(self.x + direction[0], self.y + direction[1])

Coord = Tuple[int, int]


# class Element(NamedTuple):
#     coord: Coord
#     direction: Direction
#     direction_count: int

#     def __lt__(self, other: "Element"):
#         # We don't really care about the order, but we need to be able to compare elements
#         return self.direction_count < other.direction_count

Element = Tuple[Coord, Direction, int]


def read_input(filename: str) -> List[List[int]]:
    with open(filename, "r") as f:
        return [list(map(int, list(line.strip()))) for line in f.readlines()]


def find_shortest_path(
    matrix: List[List[int]],
    max_direction_count: int = 3,
    min_direction_count: int = 1,
    start: Coord = (0, 0),
    end: Optional[Coord] = None,
) -> int:
    if end is None:
        end = (len(matrix[0]) - 1, len(matrix) - 1)
    candidates: List[Tuple[int, Element]] = []
    for dir in [UP, RIGHT, DOWN, LEFT]:
        heapq.heappush(candidates, (0, (start, dir, 1)))
    certains = set()
    iter = 0
    while candidates:
        iter += 1
        if iter % 100_000 == 0:
            print(f"Iteration {iter}")
        cost, current = heapq.heappop(candidates)
        if current in certains:
            continue
        certains.add(current)
        new_coord = (current[0][0] + current[1][0], current[0][1] + current[1][1])
        if new_coord[0] < 0 or new_coord[0] >= len(matrix[0]) or new_coord[1] < 0 or new_coord[1] >= len(matrix):
            continue
        new_cost = cost + matrix[new_coord[1]][new_coord[0]]
        if min_direction_count <= current[2] <= max_direction_count and new_coord == end:
            return new_cost
        for new_direction in [UP, RIGHT, DOWN, LEFT]:
            if new_direction[0] == 0 - current[1][0] and new_direction[1] == 0 - current[1][1]:
                continue
            new_direction_count = current[2] + 1 if new_direction == current[1] else 1
            if new_direction_count > max_direction_count or (
                current[1] != new_direction and current[2] < min_direction_count
            ):
                continue
            heapq.heappush(candidates, (new_cost, (new_coord, new_direction, new_direction_count)))
    return -1


def part_A(input_filename: str) -> int:
    matrix = read_input(input_filename)
    return find_shortest_path(matrix)


def part_B(input_filename: str) -> int:
    matrix = read_input(input_filename)
    return find_shortest_path(matrix, max_direction_count=10, min_direction_count=4)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected: 855

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected: 980


if __name__ == "__main__":
    main()
