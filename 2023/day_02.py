"""
Advent of Code 2023
--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

"""
from dataclasses import dataclass
from typing import Any, Callable, List, Dict
from aoc_performance import aoc_perf
import re

DAY = "02"

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclass
class Game:
    id: int
    blue: int = 0
    green: int = 0
    red: int = 0

    def __init__(self, input: str) -> None:
        game, subsets = input.split(":")
        self.id = int(game.split(" ")[1])
        for subset in subsets.split(";"):
            for color in subset.split(","):
                count, color_name = color.strip().split(" ")
                count = int(count)
                if color_name == "blue":
                    self.blue = max(self.blue, count)
                elif color_name == "green":
                    self.green = max(self.green, count)
                elif color_name == "red":
                    self.red = max(self.red, count)


def read_input(input_filename: str) -> List[Game]:
    return [Game(line) for line in open(input_filename, "r")]


def part_A(input_filename: str) -> int:
    games = read_input(input_filename)
    return sum(game.id for game in games if game.red <= MAX_RED and game.green <= MAX_GREEN and game.blue <= MAX_BLUE)


def part_B(input_filename: str) -> int:
    games = read_input(input_filename)
    return sum(game.red * game.green * game.blue for game in games)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
