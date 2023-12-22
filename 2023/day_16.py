"""
Advent of Code 2023
--- Day 16: The Floor Will Be Lava ---
https://adventofcode.com/2023/day/16

"""
from enum import Enum
from typing import List, Dict, NamedTuple, Set, Tuple
from aoc_performance import aoc_perf


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
mirrors: Dict[Position, str] = {}

next_direction: Dict[str, Dict[Direction, List[Direction]]] = {
    "/": {
        Direction.RIGHT: [Direction.UP],
        Direction.LEFT: [Direction.DOWN],
        Direction.UP: [Direction.RIGHT],
        Direction.DOWN: [Direction.LEFT],
    },
    "\\": {
        Direction.RIGHT: [Direction.DOWN],
        Direction.LEFT: [Direction.UP],
        Direction.UP: [Direction.LEFT],
        Direction.DOWN: [Direction.RIGHT],
    },
    "-": {
        Direction.UP: [Direction.LEFT, Direction.RIGHT],
        Direction.DOWN: [Direction.LEFT, Direction.RIGHT],
    },
    "|": {
        Direction.LEFT: [Direction.UP, Direction.DOWN],
        Direction.RIGHT: [Direction.UP, Direction.DOWN],
    },
}


def load_input(input_filename: str) -> None:
    global grid, bound_x, bound_y, mirrors
    with open(input_filename, "r") as input_file:
        grid = [list(line.strip()) for line in input_file.readlines()]
    bound_y = len(grid)
    bound_x = len(grid[0])
    mirrors = {Position(x, y): col for y, row in enumerate(grid) for x, col in enumerate(row) if col != "."}


def get_next_test(pos: Position, direction: Direction) -> Tuple[Position, Direction]:
    return Position(pos.x + direction.value[0], pos.y + direction.value[1]), direction


def count_energized(start_pos: Position, start_direction: Direction) -> int:
    queue: List[Tuple[Position, Direction]] = [(start_pos, start_direction)]
    energized: Set[Tuple[Position, Direction]] = set()

    while queue:
        pos, direction = queue.pop()
        if pos.x < 0 or pos.x >= bound_x or pos.y < 0 or pos.y >= bound_y:
            continue
        if (pos, direction) in energized:
            continue
        energized.add((pos, direction))
        # # V1 : all in one
        # queue.extend(
        #     get_next_test(pos, next_dir)
        #     for next_dir in next_direction.get(grid[pos.y][pos.x], {}).get(direction, [direction])
        # )

        # # V2 : use set of mirrors to avoid checking for empty space
        # if pos not in mirrors:
        #     queue.append((Position(pos.x + direction.value[0], pos.y + direction.value[1]), direction))
        #     continue
        # queue.extend(
        #     get_next_position(pos, next_dir) for next_dir in next_direction[mirrors[pos]].get(direction, [direction])
        # )

        # V3 : use conditions instead of dict
        match mirrors.get(pos, "."):
            case "/":
                if direction == Direction.RIGHT:
                    queue.append((Position(pos.x, pos.y - 1), Direction.UP))
                elif direction == Direction.LEFT:
                    queue.append((Position(pos.x, pos.y + 1), Direction.DOWN))
                elif direction == Direction.UP:
                    queue.append((Position(pos.x + 1, pos.y), Direction.RIGHT))
                elif direction == Direction.DOWN:
                    queue.append((Position(pos.x - 1, pos.y), Direction.LEFT))
                continue
            case "\\":
                if direction == Direction.RIGHT:
                    queue.append((Position(pos.x, pos.y + 1), Direction.DOWN))
                elif direction == Direction.LEFT:
                    queue.append((Position(pos.x, pos.y - 1), Direction.UP))
                elif direction == Direction.UP:
                    queue.append((Position(pos.x - 1, pos.y), Direction.LEFT))
                elif direction == Direction.DOWN:
                    queue.append((Position(pos.x + 1, pos.y), Direction.RIGHT))
                continue
            case "-":
                if direction in {Direction.UP, Direction.DOWN}:
                    queue.append((Position(pos.x - 1, pos.y), Direction.LEFT))
                    queue.append((Position(pos.x + 1, pos.y), Direction.RIGHT))
                    continue
            case "|":
                if direction in {Direction.LEFT, Direction.RIGHT}:
                    queue.append((Position(pos.x, pos.y - 1), Direction.UP))
                    queue.append((Position(pos.x, pos.y + 1), Direction.DOWN))
                    continue
        queue.append(get_next_test(pos, direction))

    # display_grid({pos[0] for pos in energized})
    return len({pos[0] for pos in energized})


def display_grid(lights: Set[Position]) -> None:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if Position(x, y) in lights:
                print("#", end="")
            else:
                print(col, end="")
        print()
    print()


def part_A(input_filename: str) -> int:
    load_input(input_filename)
    return count_energized(Position(0, 0), Direction.RIGHT)


def part_B(input_filename: str) -> int:
    load_input(input_filename)
    max_lights = [count_energized(Position(0, y), Direction.RIGHT) for y in range(bound_y)]
    max_lights.extend([count_energized(Position(bound_x - 1, y), Direction.LEFT) for y in range(bound_y)])
    max_lights.extend([count_energized(Position(x, 0), Direction.DOWN) for x in range(bound_x)])
    max_lights.extend([count_energized(Position(x, bound_y - 1), Direction.UP) for x in range(bound_x)])
    return max(max_lights)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected: 7236

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected: 7521


if __name__ == "__main__":
    main()
