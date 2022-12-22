# -*- coding: utf-8 -*-
""" 
--- Day 15: Beacon Exclusion Zone ---
https://adventofcode.com/2022/day/15

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

"""
DAY = "15"

from aoc_performance import aoc_perf
from typing import List, Dict, Tuple, Set
import re
from shapely.geometry import Polygon, LineString, MultiPolygon
import matplotlib.pyplot as plt


class Map:
    sensors: Set[Tuple] = set()
    beacons: Set[Tuple] = set()

    def __init__(self, filename) -> None:
        with open(filename, "r") as f:
            for line in f:
                self.process_line(line)

    def process_line(self, line: str):
        sensor_x, sensor_y, beacon_x, beacon_y = map(
            int,
            re.match(r"Sensor at x=([\d-]+), y=([\d-]+): closest beacon is at x=([\d-]+), y=([\d-]+)", line).groups(),
        )
        distance = self.manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        self.sensors.add((sensor_x, sensor_y, distance))
        self.beacons.add((beacon_x, beacon_y))

    def count_not_beacon_on_line(self, line_no: int) -> int:
        all_lines = LineString()
        for sensor_x, sensor_y, distance in self.sensors:
            remaining_dist = distance - abs(line_no - sensor_y)
            if remaining_dist > 0:
                new_line = LineString([(sensor_x - remaining_dist, line_no), (sensor_x + remaining_dist, line_no)])
                all_lines = all_lines.union(new_line)
        return int(all_lines.length)

    @staticmethod
    def manhattan_distance(from_x: int, from_y: int, to_x: int, to_y: int) -> int:
        return abs(from_x - to_x) + abs(from_y - to_y)


def part_one(filename: str, line_search: int = 10) -> int:
    map = Map(filename)
    answer: int = map.count_not_beacon_on_line(line_search)
    return answer


def part_two(filename: str, map_size: int = 20, tuning_frequency: int = 4_000_000, plot: bool = False) -> int:
    map = Map(filename)
    polygon = Polygon()
    for sensor in map.sensors:
        # For each sensor, draw the corresponding polygon.
        x, y, d = sensor
        new_polygon = Polygon([(x - d, y), (x, y + d), (x + d, y), (x, y - d)])
        polygon = polygon.union(new_polygon)
        if plot:
            plt.plot(*new_polygon.exterior.xy)

    map_polygon = Polygon([(0, 0), (0, map_size), (map_size, map_size), (map_size, 0)])
    if plot:
        plt.plot(*map_polygon.exterior.xy, color="gray")
        plt.fill(*map_polygon.exterior.xy, color="lightgray")
    result = map_polygon.difference(polygon)
    if type(result) == MultiPolygon:
        for poly in result.geoms:
            exterior = poly.exterior.coords
            # Search for a square.
            if exterior[0][0] == exterior[2][0] and exterior[1][1] == exterior[3][1]:
                result = poly
                break
    answer_x = int(result.exterior.coords[0][0] + result.exterior.coords[2][0]) // 2
    answer_y = int(result.exterior.coords[1][1] + result.exterior.coords[3][1]) // 2
    if plot:
        plt.plot(answer_x, answer_y, "+", color="black")
        plt.text(answer_x, answer_y, f"distress beacon\n  x: {answer_x}\n  y: {answer_y}", fontsize=14, color="black")
        plt.show()
    answer = answer_x * tuning_frequency + answer_y
    return answer


def main() -> None:
    input_filename, line_search, map_size = f"day_{DAY}_input_sample.txt", 10, 20
    input_filename, line_search, map_size = f"day_{DAY}_input.txt", 2_000_000, 4_000_000

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one(input_filename, line_search)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename, map_size, plot=True)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
