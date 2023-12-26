"""
Advent of Code 2023

https://adventofcode.com/2023/day/24

"""
import itertools
from typing import Any, Callable, List, Dict, Optional, Tuple
from aoc_performance import aoc_perf
import re

DAY = "24"

Point = Tuple[int, int]  # x, y
Point3D = Tuple[int, int, int]  # x, y, z
Vector = Tuple[int, int]  # x, y
Vector3D = Tuple[int, int, int]  # x, y, z
Line = Tuple[Point, Vector]
Intersection = Tuple[Optional[float], Optional[float]]


def read_input(input_filename: str) -> List[Line]:
    lines = []
    with open(input_filename, "r") as f:
        for line in f:
            if res := re.match(r"(\d+), (\d+), (\d+) @ ([-\d]+),\s*([-\d]+),\s*([-\d]+)", line.strip()):
                x, y, z, vx, vy, vz = map(int, res.groups())
                point = (x, y)
                vector = (vx, vy)
                lines.append((point, vector))
    return lines


def intersection_point(point1: Point, vector1: Vector, point2: Point, vector2: Vector) -> Intersection:
    # Decomposing points and vectors into x and y components
    x1, y1 = point1
    x2, y2 = point2
    vx1, vy1 = vector1
    vx2, vy2 = vector2

    # Calculating parameters for the equation system
    # t * vector1 + point1 = s * vector2 + point2
    t_numerator = (x2 - x1) * vy2 - (y2 - y1) * vx2
    s_numerator = (x2 - x1) * vy1 - (y2 - y1) * vx1
    denominator = vx1 * vy2 - vy1 * vx2

    # Checking for collinearity of vectors (no solution if vectors are collinear)
    if denominator == 0:
        return None, None

    # Calculating parameters t and s
    t = t_numerator / denominator
    s = s_numerator / denominator

    # Calculating the intersection point
    intersection_x = x1 + t * vx1
    intersection_y = y1 + t * vy1

    return intersection_x, intersection_y


def is_point_in_future(point: Point, vector: Vector, future_point: Intersection) -> bool:
    if future_point[0] is None:
        return False
    x, y = point
    vx, vy = vector
    fx, fy = future_point
    return (fx - x) * vx >= 0 and (fy - y) * vy >= 0


def future_intersection_point(point1: Point, vector1: Vector, point2: Point, vector2: Vector) -> Intersection:
    intersection_x, intersection_y = intersection_point(point1, vector1, point2, vector2)
    if intersection_x is None:
        return None, None
    if is_point_in_future(point1, vector1, (intersection_x, intersection_y)) and is_point_in_future(
        point2, vector2, (intersection_x, intersection_y)
    ):
        return intersection_x, intersection_y
    return None, None


def is_point_in_window(point: Intersection, window: Tuple[Point, Point]) -> bool:
    if point[0] is None:
        return False
    x, y = point
    x1, y1 = window[0]
    x2, y2 = window[1]
    return x1 <= x <= x2 and y1 <= y <= y2


def part_A(
    input_filename: str,
    window: Tuple[Point, Point] = ((200000000000000, 200000000000000), (400000000000000, 400000000000000)),
) -> int:
    lines = read_input(input_filename)
    total = 0
    for i, j in itertools.combinations(range(len(lines)), 2):
        if p := future_intersection_point(lines[i][0], lines[i][1], lines[j][0], lines[j][1]):
            if is_point_in_window(p, window):
                # print(f"Intersection between {i} and {j}")
                # print(p)
                total += 1
    return total


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
