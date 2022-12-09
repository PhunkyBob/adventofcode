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
    head: Position
    tail: Position
    tail_history: List[Position]
    filename: str

    DIRECTIONS: dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    def __init__(self, filename) -> None:
        self.filename = filename
        self.head = Position()
        self.tail = Position()
        self.tail_history = []
        self.save_tail_history()

    def play(self) -> None:
        for direction, length in self.get_motions():
            self.move_head_length(direction, length)

    def move_head_length(self, direction: str, length: int) -> None:
        for _ in range(length):
            self.move_head(direction)

    def move_head(self, direction: str):
        old_head = self.head.copy()
        self.head.move(*self.DIRECTIONS[direction])
        if not self.head.is_touching(self.tail):
            self.tail = old_head
        self.save_tail_history()

    def move_tail(self):
        pass

    def get_motions(self):
        with open(self.filename, "r") as f:
            for line in f:
                direction, length = line.split(" ")
                yield direction, int(length)

    def save_tail_history(self) -> None:
        self.tail_history.append(self.tail)

    def printmap(self):
        print(self.head)


def part_one(filename: str) -> int:
    motions = Motions(filename)
    motions.play()
    answer = len(set([(elem.x, elem.y) for elem in motions.tail_history]))
    # Code
    return answer


def part_two(filename: str) -> int:
    # Code
    return


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
