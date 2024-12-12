"""
Advent of Code 2024
--- Day 8: Resonant Collinearity ---
https://adventofcode.com/2024/day/8

............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............

--> 

......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
"""

from typing import Any, Callable, Dict, List, Set, Tuple
from aoc_performance import aoc_perf
from collections import defaultdict
from itertools import combinations

DAY = "08"
Position = Tuple[int, int]

GRID_WIDTH = 0
GRID_HEIGHT = 0


def read_input(input_filename: str) -> Dict[str, Set[Position]]:
    global GRID_WIDTH, GRID_HEIGHT
    antennas: Dict[str, Set[Position]] = defaultdict(set)
    with open(input_filename, "r") as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char != ".":
                    antennas[char].add((x, y))
    GRID_WIDTH = x
    GRID_HEIGHT = y
    return antennas


def is_out_of_bounds(position: Position) -> bool:
    x, y = position
    return x < 0 or x > GRID_WIDTH or y < 0 or y > GRID_HEIGHT


def get_antinodes_A(antennas: Dict[str, Set[Position]]) -> Set[Position]:
    antinodes: Set[Position] = set()
    for antenna in antennas.values():
        for a1, a2 in combinations(antenna, 2):
            x1, y1 = a1
            x2, y2 = a2
            diff_x = x2 - x1
            diff_y = y2 - y1
            for antinode in [(x1 - diff_x, y1 - diff_y), (x2 + diff_x, y2 + diff_y)]:
                if not is_out_of_bounds(antinode):
                    antinodes.add(antinode)
    return antinodes


def get_antinodes_B(antennas: Dict[str, Set[Position]]) -> Set[Position]:
    antinodes: Set[Position] = set()
    for antenna in antennas.values():
        for a1, a2 in combinations(antenna, 2):
            antinodes.add(a1)
            antinodes.add(a2)
            x1, y1 = a1
            x2, y2 = a2
            diff_x = x2 - x1
            diff_y = y2 - y1
            test_pos = (x1 - diff_x, y1 - diff_y)
            while not is_out_of_bounds(test_pos):
                antinodes.add(test_pos)
                test_pos = (test_pos[0] - diff_x, test_pos[1] - diff_y)
            test_pos = (x2 + diff_x, y2 + diff_y)
            while not is_out_of_bounds(test_pos):
                antinodes.add(test_pos)
                test_pos = (test_pos[0] + diff_x, test_pos[1] + diff_y)
    return antinodes


def print_map(antennas: Dict[str, Set[Position]], antinodes: Set[Position]) -> None:
    positions: Dict[Position, str] = {}
    for name, antenna in antennas.items():
        for position in antenna:
            positions[position] = name
    for y in range(GRID_HEIGHT + 1):
        for x in range(GRID_WIDTH + 1):
            if (x, y) in positions:
                print(positions[(x, y)], end="")
                continue
            if (x, y) in antinodes:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part_A(input_filename: str) -> int:
    antennas = read_input(input_filename)
    antinodes = get_antinodes_A(antennas)
    print_map(antennas, antinodes)
    return len(antinodes)


def part_B(input_filename: str) -> int:
    antennas = read_input(input_filename)
    antinodes = get_antinodes_B(antennas)
    # print_map(antennas, antinodes)
    return len(antinodes)


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
