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
        items_on_line: Set = set()
        for sensor_x, sensor_y, distance in self.sensors:
            remaining_dist = distance - abs(line_no - sensor_y)
            for i in range(remaining_dist + 1):
                if (sensor_x + i, line_no) not in self.beacons:
                    items_on_line.add(sensor_x + i)
                if (sensor_x - i, line_no) not in self.beacons:
                    items_on_line.add(sensor_x - i)
        return len(items_on_line)

    @staticmethod
    def manhattan_distance(from_x: int, from_y: int, to_x: int, to_y: int) -> int:
        return abs(from_x - to_x) + abs(from_y - to_y)


def part_one(filename: str) -> int:
    map = Map(filename)
    # answer: int = map.count_not_beacon_on_line(10)
    answer: int = map.count_not_beacon_on_line(2000000)
    return answer


def part_two(filename: str) -> int:
    map = Map(filename)
    answer = 0
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
