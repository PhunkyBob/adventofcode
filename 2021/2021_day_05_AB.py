# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/5 """

import time
from dataclasses import dataclass
from itertools import product
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    from_point: Point
    to_point: Point

    def get_hv_line(self):
        """
        Returns the points of the horizontal or vertical line.
        """
        if self.from_point.x == self.to_point.x:
            min_y = min(self.from_point.y, self.to_point.y)
            max_y = max(self.from_point.y, self.to_point.y)
            return [(self.from_point.x, y) for y in range(min_y, max_y + 1)]
        elif self.from_point.y == self.to_point.y:
            min_x = min(self.from_point.x, self.to_point.x)
            max_x = max(self.from_point.x, self.to_point.x)
            return [(x, self.from_point.y) for x in range(min_x, max_x + 1)]
        else:
            return []

    def get_diag_line(self):
        """
        Returns the points of the diag line.
        """
        if self.from_point.x == self.to_point.x or self.from_point.y == self.to_point.y:
            return []
        dx = 1 if self.to_point.x > self.from_point.x else -1
        dy = 1 if self.to_point.y > self.from_point.y else -1

        return [
            (x, y)
            for x, y in zip(
                range(self.from_point.x, self.to_point.x + dx, dx),
                range(self.from_point.y, self.to_point.y + dy, dy),
            )
        ]

    def get_line(self):
        return self.get_hv_line() + self.get_diag_line()


def load_input(filename):
    input = []
    with open(filename, "r") as f:
        for line in f:
            fr, to = line.strip().split(" -> ")
            fr_x, fr_y = fr.split(",")
            to_x, to_y = to.split(",")
            elem = Line(Point(int(fr_x), int(fr_y)), Point(int(to_x), int(to_y)))
            input.append(elem)
    return input


def draw_map_txt(points):
    min_x = 0
    min_y = 0
    max_x = max(point[0] for point in points)
    max_y = max(point[1] for point in points)
    cur_line = ""
    for y, x in product(range(min_y, max_y + 1), range(min_x, max_x + 1)):
        if x == 0:
            print(cur_line)
            cur_line = ""
        if (x, y) in points:
            cur_line += str(points[(x, y)])
        else:
            cur_line += "."
    print(cur_line)


def draw_map(points):
    min_x = 0
    min_y = 0
    max_x = max(point[0] for point in points)
    max_y = max(point[1] for point in points)
    full_map = np.zeros((max_y + 1, max_x + 1), dtype=int)
    for y, x in product(range(min_y, max_y + 1), range(min_x, max_x + 1)):
        if (x, y) in points:
            full_map[y, x] = points[(x, y)]
    plt.imshow(full_map, cmap="YlOrRd")
    plt.show()


def solve_part_one(input, draw=False):
    used_points = defaultdict(int)
    for line in input:
        for point in line.get_hv_line():
            used_points[point] += 1

    if draw:
        draw_map(used_points)
    return sum(1 if used_points[point] >= 2 else 0 for point in used_points)


def solve_part_two(input, draw=False):
    used_points = defaultdict(int)
    for line in input:
        for point in line.get_line():
            used_points[point] += 1
    
    if draw:
        draw_map(used_points)
    return sum(1 if used_points[point] >= 2 else 0 for point in used_points)


if __name__ == "__main__":
    start_time = time.time()

    draw = True

    # input_file = "2021_day_05_input_sample.txt"
    input_file = "2021_day_05_input.txt"
    input = load_input(input_file)

    """Part One"""
    result = solve_part_one(input, draw)
    print(f"Day 5 Part One: {result}")

    """Part Two"""
    result = solve_part_two(input, draw)
    print(f"Day 5 Part Two: {result}")

    print("--- %.2f seconds ---" % (time.time() - start_time))
