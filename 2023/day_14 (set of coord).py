"""
Advent of Code 2023

https://adventofcode.com/2023/day/14

"""
from enum import Enum
from functools import lru_cache
from typing import Any, Callable, List, Dict, NamedTuple, Set, Tuple
from aoc_performance import aoc_perf

DAY = "14"


class Coord(NamedTuple):
    x: int
    y: int


class Direction(Enum):
    NORTH = Coord(0, -1)
    EAST = Coord(1, 0)
    SOUTH = Coord(0, 1)
    WEST = Coord(-1, 0)


def read_input(input_filename: str) -> Tuple[Set[Coord], Set[Coord]]:
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()
    rounds = {Coord(col, row) for row, line in enumerate(lines) for col, char in enumerate(line) if char == "O"}
    cubes = {Coord(col, row) for row, line in enumerate(lines) for col, char in enumerate(line) if char == "#"}
    return rounds, cubes


def get_north_limit(coord: Coord, rounds: Set[Coord], cubes: Set[Coord]) -> Coord:
    index = limit_y = coord.y
    # filtered_cubes = set(filter(lambda x: x.x == coord.x and x.y < coord.y, cubes))
    while index >= 0 and Coord(coord.x, index) not in cubes:
        if Coord(coord.x, index) not in rounds:
            limit_y = index
        index -= 1
    return Coord(coord.x, limit_y)


# @lru_cache
def tilt_north(rounds: Set[Coord], cubes: Dict[int, Set[Coord]]) -> Set[Coord]:
    rounds_copy = set(rounds)
    split_rounds = {}
    for round in rounds:
        if round.x not in split_rounds:
            split_rounds[round.x] = []
        split_rounds[round.x].append(round)
    for current_round in rounds_copy:
        new_round = get_north_limit(
            current_round, split_rounds.get(current_round.x, set()), cubes.get(current_round.x, set())
        )
        if current_round != new_round:
            rounds.remove(current_round)
            rounds.add(new_round)
            split_rounds[current_round.x].remove(current_round)
            split_rounds[current_round.x].append(new_round)
            # print(round, new_round)
            # display(rounds, cubes)
            # print()
    return rounds


def display(rounds: Set[Coord], cubes: Set[Coord]) -> None:
    max_y = max(rounds, key=lambda coord: coord.y).y
    max_y = max(max_y, max(cubes, key=lambda coord: coord.y).y)
    max_x = max(rounds, key=lambda coord: coord.x).x
    max_x = max(max_x, max(cubes, key=lambda coord: coord.x).x)

    for row in range(max_y + 1):
        for col in range(max_x + 1):
            coord = Coord(col, row)
            if coord in cubes:
                print("#", end="")
            elif coord in rounds:
                print("O", end="")
            else:
                print(".", end="")
        print()


def get_total_load(rounds: Set[Coord], cubes: Set[Coord]) -> int:
    max_y = max(rounds, key=lambda coord: coord.y).y
    max_y = max(max_y, max(cubes, key=lambda coord: coord.y).y) + 1
    return sum(max_y - coord.y for coord in rounds)


def rotate(coords: Set[Coord], max_x: int, max_y: int) -> Set[Coord]:
    """Rotate a matrix 90 degrees clockwise."""
    return {Coord(max_y - coord.y, coord.x) for coord in coords}


def part_A(input_filename: str) -> int:
    rounds, cubes = read_input(input_filename)
    split_cubes = {}
    for cube in cubes:
        if cube.x not in split_cubes:
            split_cubes[cube.x] = []
        split_cubes[cube.x].append(cube)
    # display(rounds, cubes)
    # print()
    new_rounds = tilt_north(rounds, split_cubes)
    # display(new_rounds, cubes)
    return get_total_load(new_rounds, cubes)


def part_B(input_filename: str) -> int:
    rounds, cubes = read_input(input_filename)
    max_y = max(rounds, key=lambda coord: coord.y).y
    max_y = max(max_y, max(cubes, key=lambda coord: coord.y).y)
    max_x = max(rounds, key=lambda coord: coord.x).x
    max_x = max(max_x, max(cubes, key=lambda coord: coord.x).x)

    # Combination of cubes
    pre_cubes = {}
    for i in range(4):
        split_cubes = {}
        for cube in cubes:
            if cube.x not in split_cubes:
                split_cubes[cube.x] = []
            split_cubes[cube.x].append(cube)
        pre_cubes[i] = split_cubes
        cubes = rotate(cubes, max_x, max_y)

    memory: Dict[Tuple, int] = {}
    i = 0
    steps = 1000000000
    while i < steps:
        key = tuple(rounds)
        if key in memory:
            print(f"Found a match: step {i} == step {memory[key]}")
            loop_size = i - memory[key]
            remains = (steps - i) % loop_size
            i = steps - remains
        for j in range(4):
            new_rounds = tilt_north(rounds, pre_cubes[j])
            rounds = rotate(new_rounds, max_x, max_y)
            # cubes = rotate(cubes, max_x, max_y)
        memory[key] = i
        if i % 10 == 0:
            print(f"Round {i}")
        i += 1
    # display(rounds, cubes)

    return get_total_load(rounds, cubes)


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
