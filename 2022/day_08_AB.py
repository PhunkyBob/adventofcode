# -*- coding: utf-8 -*-
""" 
--- Day 8: Treetop Tree House ---
https://adventofcode.com/2022/day/8

First, determine whether there is enough tree cover here to keep a tree 
house hidden. To do this, you need to count the number of trees that are 
visible from outside the grid when looking directly along a row or column.

30373
25512
65332
33549
35390


- The top-left 5 is visible from the left and top. (It isn't visible 
from the right or bottom since other trees of height 5 are in the way.)
- The top-middle 5 is visible from the top and right.
- The top-right 1 is not visible from any direction; for it to be 
visible, there would need to only be trees of height 0 between it and 
an edge.
- The left-middle 5 is visible, but only from the right.
- The center 3 is not visible from any direction; for it to be visible, 
there would need to be only trees of at most height 2 between it and an 
edge.
- The right-middle 3 is visible from the right.
- In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a 
total of 21 trees are visible in this arrangement.
"""
DAY = "08"

from aoc_performance import aoc_perf
from dataclasses import dataclass, field
from typing import List
from functools import reduce


@dataclass
class Tree:
    height: int
    visible_from: List[bool] = field(default_factory=lambda: [False] * 4)
    viewing_distance: List[int] = field(default_factory=lambda: [0] * 4)
    TOP: int = 0
    LEFT: int = 1
    BOTTOM: int = 2
    RIGHT: int = 3
    _scenic_score: int = None

    def is_visible(self):
        return any([*self.visible_from])

    def scenic_score(self):
        if not self._scenic_score:
            self._scenic_score = reduce(lambda x, y: x * y, [*self.viewing_distance])
        return self._scenic_score

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.height == other.height

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


class Map:
    trees: List[List[Tree]]

    def __init__(self, filename) -> None:
        self.trees = []
        with open(filename, "r") as f:
            self.trees.extend([Tree(int(char)) for char in line] for line in map(lambda x: x.strip(), f))

    def __str__(self) -> str:
        value: str = ""
        for line in self.trees:
            for tree in line:
                value += str(tree.height)
            value += "\n"
        return value

    def get(self, x: int, y: int) -> Tree:
        return self.trees[y][x]

    def iter(self) -> Tree:
        for x in range(len(self.trees[0])):
            for y in range(len(self.trees)):
                yield self.get(x, y)

    def update_visible_from(self):
        directions = {(Tree.TOP, Tree.LEFT): (1, 1), (Tree.BOTTOM, Tree.RIGHT): (-1, -1)}
        for (axis_vertical, axis_horizontal), (dir_vertical, dir_horizontal) in directions.items():
            max_in_row = [-1] * len(self.trees[0])
            for line in self.trees[::dir_vertical]:
                max_in_line = -1
                for index, tree in enumerate(line[::dir_horizontal]):
                    if tree.height > max_in_line:
                        max_in_line = tree.height
                        tree.visible_from[axis_horizontal] = True
                    if tree.height > max_in_row[index]:
                        max_in_row[index] = tree.height
                        tree.visible_from[axis_vertical] = True

    def update_viewing_distance(self):
        for x in range(len(self.trees[0])):
            for y in range(len(self.trees)):
                self.update_viewing_distance_tree(x, y)

    def update_viewing_distance_tree(self, x: int, y: int):
        directions = {Tree.BOTTOM: (1, 0), Tree.RIGHT: (0, 1), Tree.TOP: (-1, 0), Tree.LEFT: (0, -1)}
        for axis, (dir_vertical, dir_horizontal) in directions.items():
            visibility = 0
            test_x = x + dir_horizontal
            test_y = y + dir_vertical
            while not self.is_out_of_bounds(test_x, test_y):
                visibility += 1
                if self.get(test_x, test_y) >= self.get(x, y):
                    break
                test_x += dir_horizontal
                test_y += dir_vertical
            self.trees[y][x].viewing_distance[axis] = visibility

    def is_out_of_bounds(self, x, y):
        return x < 0 or x >= len(self.trees[0]) or y < 0 or y >= len(self.trees)


def part_one(filename: str) -> int:
    my_map = Map(filename)
    my_map.update_visible_from()
    return sum(tree.is_visible() for line in my_map.trees for tree in line)


def part_two(filename: str) -> int:
    my_map = Map(filename)
    my_map.update_viewing_distance()
    return max(tree.scenic_score() for tree in my_map.iter())


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
