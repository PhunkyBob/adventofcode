"""
Advent of Code 2023

https://adventofcode.com/2023/day/16

"""
from enum import Enum
from typing import Any, Callable, List, Dict, NamedTuple, Set, Tuple
from aoc_performance import aoc_perf
import sys

sys.setrecursionlimit(16385)
DAY = "16"


class Position(NamedTuple):
    x: int
    y: int


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


grid: List[List[str]] = []
bound_x: int = 0
bound_y: int = 0
done: Set[Tuple[Position, Direction]] = set()
lights: Set[Position] = set()


def load_input(input_filename: str) -> None:
    global grid, bound_x, bound_y
    with open(input_filename, "r") as input_file:
        grid = [list(line.strip()) for line in input_file.readlines()]
    bound_y = len(grid)
    bound_x = len(grid[0])


def travel(pos: Position, direction: Direction):
    global done, lights
    # print(pos, direction)
    if pos.x < 0 or pos.x >= bound_x or pos.y < 0 or pos.y >= bound_y:
        return
    # print(done)
    if (pos, direction) in done:
        return
    done.add((pos, direction))
    lights.add(pos)
    if (
        grid[pos.y][pos.x] == "."
        or (grid[pos.y][pos.x] == "|" and direction in {Direction.UP, Direction.DOWN})
        or (grid[pos.y][pos.x] == "-" and direction in {Direction.LEFT, Direction.RIGHT})
    ):
        travel(Position(pos.x + direction.value[0], pos.y + direction.value[1]), direction)
        return
    if grid[pos.y][pos.x] == "|":
        travel(Position(pos.x + Direction.UP.value[0], pos.y + Direction.UP.value[1]), Direction.UP)
        travel(Position(pos.x + Direction.DOWN.value[0], pos.y + Direction.DOWN.value[1]), Direction.DOWN)
        return
    if grid[pos.y][pos.x] == "-":
        travel(Position(pos.x + Direction.LEFT.value[0], pos.y + Direction.LEFT.value[1]), Direction.LEFT)
        travel(Position(pos.x + Direction.RIGHT.value[0], pos.y + Direction.RIGHT.value[1]), Direction.RIGHT)
        return
    if (grid[pos.y][pos.x] == "/" and direction == Direction.RIGHT) or (
        grid[pos.y][pos.x] == "\\" and direction == Direction.LEFT
    ):
        travel(Position(pos.x + Direction.UP.value[0], pos.y + Direction.UP.value[1]), Direction.UP)
        return
    if (grid[pos.y][pos.x] == "/" and direction == Direction.LEFT) or (
        grid[pos.y][pos.x] == "\\" and direction == Direction.RIGHT
    ):
        travel(Position(pos.x + Direction.DOWN.value[0], pos.y + Direction.DOWN.value[1]), Direction.DOWN)
        return
    if (grid[pos.y][pos.x] == "/" and direction == Direction.UP) or (
        grid[pos.y][pos.x] == "\\" and direction == Direction.DOWN
    ):
        travel(Position(pos.x + Direction.RIGHT.value[0], pos.y + Direction.RIGHT.value[1]), Direction.RIGHT)
        return
    if (grid[pos.y][pos.x] == "/" and direction == Direction.DOWN) or (
        grid[pos.y][pos.x] == "\\" and direction == Direction.UP
    ):
        travel(Position(pos.x + Direction.LEFT.value[0], pos.y + Direction.LEFT.value[1]), Direction.LEFT)
        return
    return


def display_grid(lights: Set[Position]) -> None:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if Position(x, y) in lights:
                print("#", end="")
            else:
                print(col, end="")
        print()


def part_A(input_filename: str) -> int:
    load_input(input_filename)
    travel(Position(0, 0), Direction.RIGHT)
    display_grid(lights)
    return len(lights)


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

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
