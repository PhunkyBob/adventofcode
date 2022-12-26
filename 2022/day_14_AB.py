# -*- coding: utf-8 -*-
""" 
--- Day 14: Regolith Reservoir ---
https://adventofcode.com/2022/day/14


"""
DAY = "14"

from aoc_performance import aoc_perf
from typing import List, Dict, Tuple, Set
from itertools import pairwise
from functools import lru_cache


@lru_cache
def sign(value: int) -> int:
    return -1 if value < 0 else 1 if value > 0 else 0


class Map:
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    floor_y: int
    with_floor: bool
    starting_point: Tuple
    walls: Set[Tuple]
    occupied: Set[Tuple]
    last_sand: Tuple = (None, None)
    current_drop: Tuple
    next_direction: Dict
    WALL: str = "#"
    START: str = "+"
    AIR: str = "."
    SAND: str = "o"
    debug: bool

    def __init__(self, input_file: str, starting_point=(500, 0), with_floor=False, debug=False) -> None:
        self.walls = set()
        self.starting_point = starting_point
        self.with_floor = with_floor
        self.next_direction = {}
        self.current_drop = starting_point
        self.debug = debug
        with open(input_file, "r") as f:
            for line in f:
                self.add_wall_to_map(line.strip())
        self.occupied = self.walls.copy()
        self._update_bounds()
        if self.debug:
            self.print_map()

    def add_wall_to_map(self, input: str) -> None:
        for coord_from, coord_to in pairwise(input.split(" -> ")):
            x_from, y_from = map(int, coord_from.split(","))
            x_to, y_to = map(int, coord_to.split(","))
            dir_x, dir_y = sign(x_to - x_from), sign(y_to - y_from)
            if dir_x == 0:
                for y in range(y_from, y_to, dir_y):
                    self.walls.add((x_to, y))
            if dir_y == 0:
                for x in range(x_from, x_to, dir_x):
                    self.walls.add((x, y_to))
        self.walls.add((x_to, y_to))

    def _update_bounds(self) -> None:
        self.min_x = self.max_x = self.starting_point[0]
        self.min_y = self.max_y = self.starting_point[1]
        for x, y in self.walls:
            if x > self.max_x:
                self.max_x = x
            if x < self.min_x:
                self.min_x = x
            if y > self.max_y:
                self.max_y = y
            if y < self.min_y:
                self.min_y = y
        self.floor_y = self.max_y + 2

    def drop_sand(self) -> bool:
        """Return True if sand is fixed, False if falling forever"""
        x, y = self.starting_point
        new_x, new_y = self.get_next_available(x, y)
        while (new_x, new_y) != (x, y) and (y < self.max_y or self.with_floor):
            x, y = new_x, new_y
            new_x, new_y = self.get_next_available(x, y)

        if self.is_occupied(new_x, new_y):
            return False
        if (new_x, new_y) == (x, y):
            self.occupied.add((new_x, new_y))
            self.last_sand = (new_x, new_y)
            if self.debug:
                self.print_map()
            return True
        return False

    def drop_sand_iter(self) -> bool:
        """Return True if sand is fixed, False if falling forever"""
        x, y = self.starting_point
        new_x, new_y = self.get_next_available(x, y)
        while (new_x, new_y) != (x, y) and (y < self.max_y or self.with_floor):
            x, y = new_x, new_y
            new_x, new_y = self.get_next_available(x, y)
            self.current_drop = (new_x, new_y)
            yield f"{new_x}, {new_y}"

        if self.is_occupied(new_x, new_y):
            yield False
        if (new_x, new_y) == (x, y):
            self.occupied.add((new_x, new_y))
            self.last_sand = (new_x, new_y)
            if self.debug:
                self.print_map()
            yield True

    def get_next(self, x: int, y: int) -> Tuple:
        new_x, new_y = x, y
        if not self.is_occupied(x, y + 1):
            new_x, new_y = x, y + 1
        elif not self.is_occupied(x - 1, y + 1):
            new_x, new_y = x - 1, y + 1
        elif not self.is_occupied(x + 1, y + 1):
            new_x, new_y = x + 1, y + 1
        return new_x, new_y

    def update_cache(self, x, y) -> None:
        new_x, new_y = self.get_next(x, y)
        self.next_direction[(x, y)] = (new_x, new_y)
        if new_x < self.min_x:
            self.min_x = new_x
        if new_x > self.max_x:
            self.max_x = new_x

    def get_next_available(self, x, y) -> Tuple:
        if (x, y) not in self.next_direction:
            self.update_cache(x, y)
        new_x, new_y = self.next_direction[(x, y)]
        if (new_x, new_y) == self.last_sand:
            self.update_cache(x, y)
            new_x, new_y = self.next_direction[(x, y)]
        return new_x, new_y

    def is_occupied(self, x, y) -> bool:
        if self.with_floor == False:
            return (x, y) in self.occupied
        return (x, y) in self.occupied or y == self.floor_y

    def print_map(self) -> None:
        max_y = self.floor_y - 1 if self.with_floor else self.max_y
        for y in range(self.min_y, max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if (x, y) in self.walls:
                    print(self.WALL, end="")
                elif (x, y) in self.occupied:
                    print(self.SAND, end="")
                elif (x, y) == self.starting_point:
                    print(self.START, end="")
                else:
                    print(self.AIR, end="")
            print()
        print()


def part_one(filename: str) -> int:
    my_map = Map(filename, debug=False)
    answer = 0
    while my_map.drop_sand():
        answer += 1
        # map.print_map()
    return answer


def part_one_step_by_step(filename: str) -> int:
    my_map = Map(filename, debug=False)
    answer = 0
    while (i := iter(my_map.drop_sand_iter())) and list(i)[-1] == True:
        answer += 1
    return answer


def part_two(filename: str) -> int:
    my_map = Map(filename, with_floor=True, debug=False)
    answer = 0
    while my_map.drop_sand():
        # if answer % 100 == 0:
        #     map.print_map()
        answer += 1
    return answer


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one_step_by_step(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
