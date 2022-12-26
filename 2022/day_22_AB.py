# -*- coding: utf-8 -*-
""" 
--- Day 22: Monkey Map ---
https://adventofcode.com/2022/day/22

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5

"""
DAY = "22"

from aoc_performance import aoc_perf
from typing import Set, Tuple, List, Dict, Deque
import re
from collections import deque
from functools import lru_cache


class Map:
    walls: Set[Tuple[int, int]]
    open_tiles: Set[Tuple[int, int]]
    position: Tuple[int, int]
    instructions: List[str | int]
    map_width: int = 0
    map_height: int = 0
    direction: str
    vectors: Dict = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
    orientation: Deque = deque(["R", "D", "L", "U"])

    def __init__(self, filename: str) -> None:
        self.walls = set()
        self.open_tiles = set()
        self.instructions = list()
        with open(filename, "r") as f:
            map_str, instructions = f.read().split("\n\n")
        self.read_map(map_str)
        self.get_initial_position(map_str)
        self.read_instructions(instructions)

    def read_map(self, map_str: str) -> None:
        for y, line in enumerate(map_str.split("\n")):
            for x, val in enumerate(line):
                if val == ".":
                    self.open_tiles.add((x, y))
                if val == "#":
                    self.walls.add((x, y))
        self.map_width, self.map_height = list(
            map(lambda x: x + 1, map(max, zip(*list(self.walls | self.open_tiles))))
        )

    def get_initial_position(self, map_str: str) -> None:
        self.position = (0, 0)
        for x, val in enumerate(map_str.split("\n")[0]):
            if val == ".":
                self.position = (x, 0)
                break

    def read_instructions(self, instructions: str) -> None:
        self.instructions = list(map(lambda x: int(x) if x.isdigit() else x, re.findall("(\d+|\w)", instructions)))

    @lru_cache
    def get_next_position(self, position: Tuple[int, int], orientation: str):
        new_position = position
        dir_x, dir_y = self.vectors[orientation]
        new_position = (
            (new_position[0] + dir_x) % self.map_width,
            (new_position[1] + dir_y) % self.map_height,
        )
        while new_position not in self.walls and new_position not in self.open_tiles:
            new_position = (
                (new_position[0] + dir_x) % self.map_width,
                (new_position[1] + dir_y) % self.map_height,
            )
        if new_position in self.open_tiles:
            return new_position
        return position

    def turn(self, direction: str) -> None:
        if direction == "R":
            self.orientation.rotate(-1)
        if direction == "L":
            self.orientation.rotate(1)

    # def follow_instructions_iter(self) -> Tuple:
    #     for val in self.instructions:
    #         if type(val) == int:
    #             for _ in range(val):
    #                 yield self.get_next_position()
    #         else:
    #             self.turn(val)
    #             yield self.position
    #     return

    def follow_instructions(self) -> None:
        for val in self.instructions:
            if type(val) == int:
                for _ in range(val):
                    self.position = self.get_next_position(self.position, self.orientation[0])
            else:
                self.turn(val)
        return


def part_one(filename: str) -> int:
    facing_values = {"R": 0, "D": 1, "L": 2, "U": 3}
    my_map = Map(filename)
    my_map.follow_instructions()
    x = my_map.position[0] + 1
    y = my_map.position[1] + 1
    answer = 1000 * y + 4 * x + facing_values[my_map.orientation[0]]

    # Code
    return answer


def part_two(filename: str) -> int:
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
