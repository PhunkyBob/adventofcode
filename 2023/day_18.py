"""
Advent of Code 2023

https://adventofcode.com/2023/day/18

"""

import itertools
from collections import deque
import sys
from typing import Any, Callable, Deque, List, Dict, Set, Tuple
from aoc_performance import aoc_perf

DAY = "18"

sys.setrecursionlimit(10**6)

Coord = Tuple[int, int]  # (x, y)
Holes = Dict[Coord, str]  # (x, y), color

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

holes: Holes = {}
outside: Set[Coord] = set()
inside: Set[Coord] = set()
min_x, max_x, min_y, max_y = 0, 0, 0, 0


def read_input(input_filename: str) -> None:
    global holes, min_x, max_x, min_y, max_y, inside, outside
    holes = {}
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    outside = set()
    inside = set()
    with open(input_filename, "r") as input_file:
        cur_x, cur_y = 0, 0
        for line in input_file:
            direction, count, color = line.strip().split(" ")
            count = int(count)
            color = color.replace("(", "").replace(")", "")
            for _ in range(count):
                cur_x += directions[direction][0]
                cur_y += directions[direction][1]
                holes[(cur_x, cur_y)] = color
    xs = [x for (x, y) in holes]
    ys = [y for (x, y) in holes]
    min_x, max_x = min(xs) - 1, max(xs) + 1
    min_y, max_y = min(ys) - 1, max(ys) + 1


def draw() -> None:
    with open("out.txt", "w") as out_file:
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in holes:
                    print("#", end="")
                    out_file.write("#")
                elif (x, y) in outside:
                    print(" ", end="")
                    out_file.write(" ")
                else:
                    print(".", end="")
                    out_file.write(".")
            print()
            out_file.write("\n")
        print()


def get_all_outside(coord: Coord) -> None:
    global outside

    to_test: Deque[Coord] = deque([coord])
    while to_test:
        cur_coord = to_test.pop()
        if cur_coord in outside:
            continue
        if cur_coord[0] < min_x or cur_coord[0] > max_x or cur_coord[1] < min_y or cur_coord[1] > max_y:
            continue
        outside.add(cur_coord)
        for direction in directions.values():
            new_coord = (cur_coord[0] + direction[0], cur_coord[1] + direction[1])
            if new_coord not in holes and new_coord not in outside:
                to_test.append(new_coord)


def part_A(input_filename: str) -> int:
    read_input(input_filename)
    get_all_outside((min_x, min_y))
    # draw()
    # get_all_outside((0, 0))
    return sum((x, y) not in outside for y, x in itertools.product(range(min_y, max_y + 1), range(min_x, max_x + 1)))


def read_input2(input_filename: str) -> List[Coord]:
    points: List[Coord] = []
    perim = 0
    with open(input_filename, "r") as input_file:
        cur_x, cur_y = 0, 0
        points.append((cur_x, cur_y))
        for line in input_file:
            _, _, color = line.strip().split(" ")
            color = color.replace("(", "").replace(")", "")
            count = int(color[1:-1], 16)
            int_to_dir = {"0": "R", "1": "D", "2": "L", "3": "U"}
            direction = int_to_dir[color[-1]]
            cur_x += directions[direction][0] * count
            cur_y += directions[direction][1] * count
            points.append((cur_x, cur_y))
            perim += count
    return points


def shoelace(points: List[Coord]) -> int:
    """https://en.wikipedia.org/wiki/Shoelace_formula"""
    n = len(points)
    return (
        abs(sum(points[i][0] * points[(i + 1) % n][1] - points[(i + 1) % n][0] * points[i][1] for i in range(n))) // 2
    )


def perimeter(points: List[Coord]) -> int:
    return sum(
        abs(points[i][0] - points[(i + 1) % len(points)][0]) + abs(points[i][1] - points[(i + 1) % len(points)][1])
        for i in range(len(points))
    )


def part_B(input_filename: str) -> int:
    points = read_input2(input_filename)
    surface = shoelace(points)
    p = perimeter(points)
    return surface + p // 2 + 1


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected: 70253

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
