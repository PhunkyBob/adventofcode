# -*- coding: utf-8 -*-
DAY = "15"

from aoc_performance import aoc_perf
import re
from shapely.geometry import Polygon, box
import matplotlib.pyplot as plt


def part_two(filename: str, plot: bool = False) -> int:
    # MAP_SIZE = 20
    MAP_SIZE = 4_000_000
    all_sensors = Polygon()
    with open(filename, "r") as f:
        for line in f:
            sensor_x, sensor_y, beacon_x, beacon_y = map(
                int,
                re.match(
                    r"Sensor at x=([\d-]+), y=([\d-]+): closest beacon is at x=([\d-]+), y=([\d-]+)", line
                ).groups(),
            )
            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            current_sensor = Polygon(
                [
                    (sensor_x - distance, sensor_y),
                    (sensor_x, sensor_y + distance),
                    (sensor_x + distance, sensor_y),
                    (sensor_x, sensor_y - distance),
                ]
            )
            if plot:
                plt.plot(*current_sensor.exterior.xy)
            all_sensors = all_sensors.union(current_sensor)

    map_polygon = box(0, 0, MAP_SIZE, MAP_SIZE)
    if plot:
        plt.plot(*map_polygon.exterior.xy, color="gray")
        plt.fill(*map_polygon.exterior.xy, color="lightgray")
    result = map_polygon.difference(all_sensors).bounds
    x = int(result[0] + 1)
    y = int(result[1] + 1)
    if plot:
        plt.plot(x, y, "+", color="black")
        plt.text(x, y, f"distress beacon\n  x: {x}\n  y: {y}", fontsize=14, color="black")
    answer = x * MAP_SIZE + y
    if plot:
        plt.show()
    return answer


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename, plot=True)
        print(f"Answer: {answer}")
        # Your puzzle answer was 13784551204480.


if __name__ == "__main__":
    main()
