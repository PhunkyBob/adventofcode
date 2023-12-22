"""
Advent of Code 2023
--- Day 16: The Floor Will Be Lava ---
https://adventofcode.com/2023/day/16

"""
from enum import Enum
from typing import List, Dict, NamedTuple, Set, Tuple
from aoc_performance import aoc_perf


DAY = "16"


# class Position(NamedTuple):
#     x: int
#     y: int

Position = Tuple[int, int]


# class Direction(Enum): # 22 seconds
Direction = Tuple[int, int]  # 15 seconds
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
        RIGHT: [UP],
        LEFT: [DOWN],
        UP: [RIGHT],
        DOWN: [LEFT],
    },
    "\\": {
        RIGHT: [DOWN],
        LEFT: [UP],
        UP: [LEFT],
        DOWN: [RIGHT],
    },
    "-": {
        UP: [LEFT, RIGHT],
        DOWN: [LEFT, RIGHT],
    },
    "|": {
        LEFT: [UP, DOWN],
        RIGHT: [UP, DOWN],
    },
}


def load_input(input_filename: str) -> None:
    global grid, bound_x, bound_y, mirrors
    with open(input_filename, "r") as input_file:
        grid = [list(line.strip()) for line in input_file.readlines()]
    bound_y = len(grid)
    bound_x = len(grid[0])
    mirrors = {(x, y): col for y, row in enumerate(grid) for x, col in enumerate(row) if col != "."}


def get_next_test(pos: Position, direction: Direction) -> Tuple[Position, Direction]:
    return (pos[0] + direction[0], pos[1] + direction[1]), direction


def count_energized(start_pos: Position, start_direction: Direction) -> int:
    queue: List[Tuple[Position, Direction]] = [(start_pos, start_direction)]
    energized: Set[Tuple[Position, Direction]] = set()

    while queue:
        pos, direction = queue.pop()
        if pos[0] < 0 or pos[0] >= bound_x or pos[1] < 0 or pos[1] >= bound_y:
            continue
        if (pos, direction) in energized:
            continue
        energized.add((pos, direction))
        # # V1 : all in one
        # queue.extend(
        #     get_next_test(pos, next_dir)
        #     for next_dir in next_direction.get(grid[pos[1]][pos[0]], {}).get(direction, [direction])
        # )

        # # V2 : use set of mirrors to avoid checking for empty space
        # if pos not in mirrors:
        #     queue.append(((pos[0] + direction[0], pos[1] + direction[1]), direction))
        #     continue
        # queue.extend(
        #     get_next_test(pos, next_dir) for next_dir in next_direction[mirrors[pos]].get(direction, [direction])
        # )

        # V3 : use conditions instead of dict
        match mirrors.get(pos, "."):
            case "/":
                if direction == RIGHT:
                    queue.append(((pos[0], pos[1] - 1), UP))
                elif direction == LEFT:
                    queue.append(((pos[0], pos[1] + 1), DOWN))
                elif direction == UP:
                    queue.append(((pos[0] + 1, pos[1]), RIGHT))
                elif direction == DOWN:
                    queue.append(((pos[0] - 1, pos[1]), LEFT))
                continue
            case "\\":
                if direction == RIGHT:
                    queue.append(((pos[0], pos[1] + 1), DOWN))
                elif direction == LEFT:
                    queue.append(((pos[0], pos[1] - 1), UP))
                elif direction == UP:
                    queue.append(((pos[0] - 1, pos[1]), LEFT))
                elif direction == DOWN:
                    queue.append(((pos[0] + 1, pos[1]), RIGHT))
                continue
            case "-":
                if direction in {UP, DOWN}:
                    queue.append(((pos[0] - 1, pos[1]), LEFT))
                    queue.append(((pos[0] + 1, pos[1]), RIGHT))
                    continue
            case "|":
                if direction in {LEFT, RIGHT}:
                    queue.append(((pos[0], pos[1] - 1), UP))
                    queue.append(((pos[0], pos[1] + 1), DOWN))
                    continue
        queue.append(get_next_test(pos, direction))

    # display_grid({pos[0] for pos in energized})
    return len({pos[0] for pos in energized})


def display_grid(lights: Set[Position]) -> None:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if (x, y) in lights:
                print("#", end="")
            else:
                print(col, end="")
        print()
    print()


def part_A(input_filename: str) -> int:
    load_input(input_filename)
    return count_energized((0, 0), RIGHT)


def part_B(input_filename: str) -> int:
    load_input(input_filename)
    max_lights = [count_energized((0, y), RIGHT) for y in range(bound_y)]
    max_lights.extend([count_energized((bound_x - 1, y), LEFT) for y in range(bound_y)])
    max_lights.extend([count_energized((x, 0), DOWN) for x in range(bound_x)])
    max_lights.extend([count_energized((x, bound_y - 1), UP) for x in range(bound_x)])
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
