"""
Advent of Code 2024
--- Day 6: Guard Gallivant ---
https://adventofcode.com/2024/day/6

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.
"""

from typing import Any, Callable, Dict, Iterator, List, Set, Tuple

from aoc_performance import aoc_perf
from enum import Enum

DAY = "06"

Position = Tuple[int, int]
DIRECTIONS: Dict[str, Position] = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}
GRID_WIDTH = 0
GRID_HEIGHT = 0


class ExitReason(Enum):
    OUT_OF_BOUNDS = 0
    ALREADY_VISITED = 1


def read_input(input_filename: str):
    global GRID_WIDTH, GRID_HEIGHT
    guard_position: Position = (0, 0)
    obstructions: Set[Position] = set()
    with open(input_filename, "r") as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char == "#":
                    obstructions.add((x, y))
                elif char == "^":
                    guard_position = (x, y)
    GRID_WIDTH = max(x for x, _ in obstructions) + 1
    GRID_HEIGHT = max(y for _, y in obstructions) + 1
    return obstructions, guard_position


def get_next_direction() -> Iterator[str]:
    while True:
        yield from ["N", "E", "S", "W"]


def print_map(obstructions: Set[Position], guard_position: Position, guard_direction: str, already_visited) -> None:
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if (x, y) == guard_position:
                print(guard_direction, end="")
            elif (x, y) in obstructions:
                print("#", end="")
            elif (x, y) in already_visited:
                print("X", end="")
            else:
                print(".", end="")
        print()


def is_out_of_bounds(position: Position) -> bool:
    x, y = position
    return x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT


def get_next_position(position: Position, direction: str) -> Position:
    dx, dy = DIRECTIONS[direction]
    x, y = position
    return (x + dx, y + dy)


def get_moves(obstructions: Set[Position], guard_position: Position) -> Tuple[Set[Position], ExitReason]:
    def is_obstructed(position: Position) -> bool:
        return position in obstructions

    direction_iter = get_next_direction()
    guard_direction = next(direction_iter)
    already_visited: Dict[Position, List[str]] = {}
    # print_map(obstructions, guard_position, guard_direction, already_visited)
    while (
        guard_position not in already_visited or guard_direction not in already_visited[guard_position]
    ) and not is_out_of_bounds(guard_position):
        already_visited.setdefault(guard_position, []).append(guard_direction)
        next_position = get_next_position(guard_position, guard_direction)
        if is_obstructed(next_position):
            guard_direction = next(direction_iter)
        else:
            guard_position = next_position
        # print_map(obstructions, guard_position, guard_direction, already_visited)
    exit_reason = ExitReason.OUT_OF_BOUNDS if is_out_of_bounds(guard_position) else ExitReason.ALREADY_VISITED
    return set(already_visited.keys()), exit_reason


def part_A(input_filename: str) -> int:
    obstructions, guard_position = read_input(input_filename)
    moves, _ = get_moves(obstructions, guard_position)
    return len(moves)


def part_B(input_filename: str) -> int:
    obstructions, guard_position = read_input(input_filename)
    moves, _ = get_moves(obstructions, guard_position)
    possible_loops = 0
    for position in moves:
        obstructions.add(position)
        _, exit_reason = get_moves(obstructions, guard_position)
        obstructions.remove(position)
        if exit_reason == ExitReason.ALREADY_VISITED:
            possible_loops += 1
    return possible_loops


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
