# -*- coding: utf-8 -*-
""" 
--- Day 9: Rope Bridge ---
https://adventofcode.com/2022/day/9

Consider a rope with a knot at each end; these knots mark the head and the 
tail of the rope. If the head moves far enough away from the tail, the tail 
is pulled toward the head.

.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....
"""
DAY = "09"

from aoc_performance import aoc_perf
from dataclasses import dataclass
from typing import List
from collections import defaultdict


@dataclass
class Position:
    x: int = 0
    y: int = 0

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def is_touching(self, elem: "Position") -> bool:
        return max(abs(self.x - elem.x), abs(self.y - elem.y)) <= 1

    def copy(self) -> "Position":
        return Position(self.x, self.y)


class Motions:
    knots: List["Position"]
    tail_history: List[Position]
    filename: str
    bounds: List[List[int]]

    DIRECTIONS: dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    def __init__(self, filename, knots: int = 2, debug=False) -> None:
        self.filename = filename
        self.knots = [Position() for _ in range(knots)]
        self.tail_history = []
        self.debug = debug
        self.get_bounds()
        if self.debug:
            print("=== Initial state ===")
            self.printmap()
        self.save_tail_history()

    def play(self) -> None:
        for direction, length in self.get_motions():
            if self.debug:
                print(f"== {direction} {length} ==")
            self.move_head_length(direction, length)
            self.printmap()

    def move_head_length(self, direction: str, length: int) -> None:
        for _ in range(length):
            self.move_head(direction)

    def move_head(self, direction: str):
        self.knots[0].move(*self.DIRECTIONS[direction])
        for i in range(len(self.knots) - 1):
            previous_knot = self.knots[i]
            actual_knot = self.knots[i + 1]
            if not previous_knot.is_touching(actual_knot):
                self.knots[i + 1].x += max(-1, min(1, previous_knot.x - actual_knot.x))
                self.knots[i + 1].y += max(-1, min(1, previous_knot.y - actual_knot.y))
        # self.printmap()
        self.save_tail_history()

    def get_motions(self):
        with open(self.filename, "r") as f:
            for line in f:
                direction, length = line.split(" ")
                yield direction, int(length)

    def save_tail_history(self) -> None:
        self.tail_history.append(self.knots[-1].copy())

    def get_bounds(self) -> None:
        if not self.debug:
            return
        if not self.filename:
            return
        min_x = max_x = min_y = max_y = 0
        x = y = 0
        with open(self.filename, "r") as f:
            for line in f:
                direction, length = line.split(" ")
                x = x + self.DIRECTIONS[direction][0] * int(length)
                y = y + self.DIRECTIONS[direction][1] * int(length)
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)
        self.bounds = [[min_x, max_x], [min_y, max_y]]

    def printmap(self):
        if not self.debug:
            return
        if not self.filename:
            return
        for y in range(self.bounds[1][1], self.bounds[1][0] - 1, -1):
            covers = defaultdict(list)
            for x in range(self.bounds[0][0], self.bounds[0][1] + 1):
                display = "."
                for i, knot in enumerate(self.knots):
                    if knot.x == x and knot.y == y:
                        if display == ".":
                            display = "H" if i == 0 else i
                        else:
                            covers[display].append(i)
                print(display, end="")
            if len(covers):
                print("   (", end="")
                print(" ; ".join([f"{k} covers {', '.join(map(str, val))}" for k, val in covers.items()]), end="")
                print(")", end="")
            print()
        print("")


def part_one(filename: str) -> int:
    motions = Motions(filename)
    motions.play()
    return len({(elem.x, elem.y) for elem in motions.tail_history})


def part_two(filename: str, debug=False) -> int:
    motions = Motions(filename, 10, debug=debug)
    motions.play()
    return len({(elem.x, elem.y) for elem in motions.tail_history})


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input_sample2.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename, debug=False)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
