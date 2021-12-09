# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/9 """

import time
from functools import reduce
from operator import mul
from itertools import product

class Heightmap:
    heightmap = []

    def __init__(self, filename) -> None:
        self.heightmap = [
            [int(y) for y in list(x.strip())] for x in open(filename, "r").readlines()
        ]

    def get_risk(self, x, y):
        for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (
                y + direction[1] >= 0
                and y + direction[1] < len(self.heightmap)
                and x + direction[0] >= 0
                and x + direction[0] < len(self.heightmap[y + direction[1]])
                and self.heightmap[y + direction[1]][x + direction[0]]
                <= self.heightmap[y][x]
            ):
                return 0
        return 1 + self.heightmap[y][x]

    def get_risk_level(self):
        return sum([self.get_risk(x, y) for x, y in product(range(len(self.heightmap[0])), range(len(self.heightmap)))])


    def get_low_points(self):
        return [(x, y) for x, y in product(range(len(self.heightmap[0])), range(len(self.heightmap))) if self.get_risk(x, y)]


    def get_basin(self, x, y, visited):
        if (x, y) in visited:
            return {}
        if x < 0 or y < 0 or x >= len(self.heightmap[0]) or y >= len(self.heightmap):
            return {}
        if self.heightmap[y][x] == 9:
            return {}

        visited[(x, y)] = True
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            visited.update(self.get_basin(x + dx, y + dy, visited))
        return visited

    def get_basin_size(self, x, y):
        basin = self.get_basin(x, y, {})
        return len(basin)


def solve_part_one(heightmap):
    return heightmap.get_risk_level()


def solve_part_two(heightmap):
    low_points = heightmap.get_low_points()
    sizes = [heightmap.get_basin_size(x, y) for x, y in low_points]
    sizes.sort(reverse=True)
    return reduce(mul, sizes[:3])


if __name__ == "__main__":
    start_time = time.time()

    # input_file = "2021_day_09_input_sample.txt"
    input_file = "2021_day_09_input.txt"
    heightmap = Heightmap(input_file)

    """Part One"""
    result = solve_part_one(heightmap)
    print(f"Day 9 Part One: {result}")
    # Your puzzle answer was 508.

    """Part Two"""
    result = solve_part_two(heightmap)
    print(f"Day 9 Part Two: {result}")
    # Your puzzle answer was 1564640.

    print("--- %.2f seconds ---" % (time.time() - start_time))
