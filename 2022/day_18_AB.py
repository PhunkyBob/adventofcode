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
from typing import List, Dict, Tuple


def read_input(filename: str):
    data: List[Tuple[int, int, int]] = []
    with open(filename, "r") as f:
        for line in map(lambda x: x.strip(), f):
            x, y, z = map(int, line.split(","))
            data.append((x, y, z))
    return data


def part_one(filename: str) -> int:
    data = read_input(filename)
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    sides_exposed = 0
    for cube in data:
        for dir in directions:
            test_x = cube[0] + dir[0]
            test_y = cube[1] + dir[1]
            test_z = cube[2] + dir[2]
            if (test_x, test_y, test_z) not in data:
                sides_exposed += 1
    return sides_exposed


def part_two(filename: str) -> int:
    data = read_input(filename)
    # Code
    return


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
