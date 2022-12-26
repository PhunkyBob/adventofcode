# -*- coding: utf-8 -*-
""" 
--- Day 18: Boiling Boulders ---
https://adventofcode.com/2022/day/18

To approximate the surface area, count the number of sides of each cube 
that are not immediately connected to another cube. So, if your scan were 
only two adjacent cubes like 1,1,1 and 2,1,1, each cube would have a single 
side covered and five sides exposed, a total surface area of 10 sides.

2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5

In the above example, after counting up all the sides that aren't connected 
to another cube, the total surface area is 64.
"""
DAY = "18"

from aoc_performance import aoc_perf
from typing import List, Dict, Tuple, Set

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def read_input(filename: str) -> Set[Tuple[int, int, int]]:
    data: Set[Tuple[int, int, int]] = {tuple(map(int, line.split(","))) for line in open(filename, "r")}
    return data


def count_exposed(existing_cubes: Set[Tuple[int, int, int]], explore_space: Set[Tuple[int, int, int]] = None) -> int:
    sides_exposed = 0
    for cube in existing_cubes:
        touche_aucun = True
        for dir in directions:
            test_x = cube[0] + dir[0]
            test_y = cube[1] + dir[1]
            test_z = cube[2] + dir[2]
            if explore_space:
                if (test_x, test_y, test_z) in explore_space:
                    sides_exposed += 1
                    touche_aucun = False
            else:
                if (test_x, test_y, test_z) not in existing_cubes:
                    sides_exposed += 1
    return sides_exposed


def part_one(filename: str) -> int:
    data = read_input(filename)
    answer = count_exposed(data)
    return answer


def part_two(filename: str) -> int:
    data = read_input(filename)

    min_x, min_y, min_z = list(map(min, zip(*data)))
    max_x, max_y, max_z = list(map(max, zip(*data)))

    cubes_to_test: Set[Tuple[int, int, int]] = set()
    cubes_to_test.add((min_x - 1, min_y - 1, min_z - 1))
    cubes_outside: Set[Tuple[int, int, int]] = set()

    while cubes_to_test:
        x, y, z = cubes_to_test.pop()
        cubes_outside.add((x, y, z))
        for dir in directions:
            test_x = x + dir[0]
            test_y = y + dir[1]
            test_z = z + dir[2]
            if (
                min_x - 1 <= test_x <= max_x + 1
                and min_y - 1 <= test_y <= max_y + 1
                and min_z - 1 <= test_z <= max_z + 1
            ):
                if (test_x, test_y, test_z) not in data and (test_x, test_y, test_z) not in cubes_outside:
                    cubes_to_test.add((test_x, test_y, test_z))
    answer = count_exposed(data, cubes_outside)
    return answer


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
