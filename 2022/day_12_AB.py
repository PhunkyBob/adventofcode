# -*- coding: utf-8 -*-
""" 
--- Day 12: Hill Climbing Algorithm ---
https://adventofcode.com/2022/day/12

You'd like to reach E, but to save energy, you should do it in as few steps 
as possible. 

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
"""
DAY = "12"

from aoc_performance import aoc_perf
import networkx as nx
from typing import List


class Map:
    data = {}
    map_width = 0
    map_height = 0
    start = (0, 0)
    best_signal = (0, 0)
    list_a: List
    graph = None

    def __init__(self, filename) -> None:
        self.data = {}
        self.map_width = 0
        self.map_height = 0
        self.start = (0, 0)
        self.best_signal = (0, 0)
        self.list_a = []
        with open(filename, "r") as f:
            y = 0
            for line in map(lambda x: x.strip(), f):
                self.map_width = len(line)
                for x, val in enumerate(line):
                    if val == "S":
                        self.start = f"{x},{y}"
                        val = "a"
                    if val == "E":
                        self.best_signal = f"{x},{y}"
                        val = "z"
                    if val == "a":
                        self.list_a.append(f"{x},{y}")
                    self.data[(x, y)] = val
                y += 1
            self.map_height = y

    def is_in_bounds(self, x, y) -> bool:
        return x >= 0 and x < self.map_width and y >= 0 and y < self.map_height

    def generate_graph(self) -> None:
        self.graph = nx.Graph().to_directed()
        directions: dict = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
        for y in range(self.map_height):
            for x in range(self.map_width):
                current_value = self.data[(x, y)]
                for dir_x, dir_y in directions.values():
                    check_x, check_y = x + dir_x, y + dir_y
                    if self.is_in_bounds(check_x, check_y):
                        test_value = self.data[(check_x, check_y)]
                        if ord(test_value) <= ord(current_value) + 1:
                            self.graph.add_edge(f"{check_x},{check_y}", f"{x},{y}")

    def distance_start_best(self) -> int:
        if not self.graph:
            self.generate_graph()
        distance = len(nx.shortest_path(self.graph, self.best_signal, self.start)) - 1
        return distance

    def distance_best_a(self) -> int:
        if not self.graph:
            self.generate_graph()
        min_distance = min(
            [
                value
                for elem, value in nx.single_source_shortest_path_length(self.graph, self.best_signal).items()
                if elem in self.list_a
            ]
        )
        return min_distance

    def save_map(self, filename):
        map_distance = nx.single_source_shortest_path_length(self.graph, self.best_signal)
        with open(filename, "w") as f:
            for y in range(self.map_height):
                for x in range(self.map_width):
                    dist = map_distance[f"{x},{y}"] if f"{x},{y}" in map_distance else "."
                    f.write(f"{dist:>4}")
                f.write("\n")


def part_one(filename: str) -> int:
    map = Map(filename)
    answer = map.distance_start_best()
    return answer


def part_two(filename: str) -> int:
    map = Map(filename)
    answer = map.distance_best_a()
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
