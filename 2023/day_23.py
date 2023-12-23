"""
Advent of Code 2023

https://adventofcode.com/2023/day/23

"""

from functools import lru_cache
import heapq
import itertools
import sys
from typing import Any, Callable, List, Dict, Set, Tuple
from aoc_performance import aoc_perf
from collections import deque

sys.setrecursionlimit(10000)


DAY = "23"

Coord = Tuple[int, int]  # (x, y, weight)
Matrix = List[List[str]]

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


def read_input(input_filename: str) -> Matrix:
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()
        return [list(line.strip()) for line in lines]


def get_edges(forest: Matrix, part_B: bool = False) -> Dict[Coord, Set[Coord]]:
    width = len(forest[0])
    height = len(forest)
    edges: Dict[Coord, Set[Coord]] = {}
    for y, x in itertools.product(range(height), range(width)):
        cell = forest[y][x]
        if (x, y) not in edges:
            edges[(x, y)] = set()
        if cell == "#":
            continue
        if not part_B:
            if cell == ">":
                edges[(x, y)].add((x + 1, y))
                continue
            if cell == "<":
                edges[(x, y)].add((x - 1, y))
                continue
            if cell == "^":
                edges[(x, y)].add((x, y - 1))
                continue
            if cell == "v":
                edges[(x, y)].add((x, y + 1))
                continue
        for direction in [UP, RIGHT, DOWN, LEFT]:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if 0 <= new_x < width and 0 <= new_y < height:
                new_cell = forest[new_y][new_x]
                if new_cell != "#":
                    edges[(x, y)].add((new_x, new_y))
    return edges


def display(forest: Matrix, path: Set[Coord]) -> None:
    for y, x in itertools.product(range(len(forest)), range(len(forest[0]))):
        if (x, y) in path:
            print("O", end="")
        else:
            print(forest[y][x], end="")
        if x == len(forest[0]) - 1:
            print()
    print()


def longest_path(edges: Dict[Coord, Set[Coord]], start: Coord, end: Coord, visited: Set[Coord]) -> int:
    if start == end:
        return 0
    longest = 0
    for edge in edges[start]:
        if edge not in visited:
            longest = max(longest, longest_path(edges, edge, end, visited.union({start})))
    return longest + 1


def longest_path_queue(edges: Dict[Coord, Set[Coord]], start: Coord, end: Coord) -> int:
    queue: List[Tuple[Coord, int, Set]] = [(start, 0, set())]  # Position, distance, visited
    heapq.heapify(queue)
    distances = []
    while queue:
        node, distance, visited = heapq.heappop(queue)
        if node == end:
            distances.append(distance)
            continue

        for edge in edges[node]:
            if edge not in visited:
                heapq.heappush(queue, (edge, distance + 1, visited | {node}))

    return max(distances)  # If no path is found


def part_A(input_filename: str) -> int:
    forest: Matrix = read_input(input_filename)
    edges = get_edges(forest)
    # return longest_path(edges, (1, 0), (len(forest[0]) - 2, len(forest) - 1), set())
    return longest_path_queue(edges, (1, 0), (len(forest[0]) - 2, len(forest) - 1))


def part_B(input_filename: str) -> int:
    return 0
    forest: Matrix = read_input(input_filename)
    edges = get_edges(forest, part_B=True)
    return longest_path_queue(edges, (1, 0), (len(forest[0]) - 2, len(forest) - 1))


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

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
