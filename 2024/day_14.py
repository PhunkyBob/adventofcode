"""
Advent of Code 2024
--- Day 14: Restroom Redoubt ---
https://adventofcode.com/2024/day/14

p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3

Each robot's position is given as p=x,y where x represents the number of tiles the robot is from the left wall and y represents the number of tiles from the top wall (when viewed from above). So, a position of p=0,0 means the robot is all the way in the top-left corner.
"""

from collections import Counter, defaultdict
from math import prod
from typing import Set, Tuple
import re
from aoc_performance import aoc_perf

DAY = "14"
Position = Tuple[int, int]
Robot = Tuple[Position, Position]


def read_input(input_filename: str) -> Set[Robot]:
    robots: Set[Robot] = set()
    with open(input_filename, "r") as file:
        for line in file:
            pos_x, pos_y, vel_x, vel_y = re.findall(r"(-?\d+)", line)
            robots.add(((int(pos_x), int(pos_y)), (int(vel_x), int(vel_y))))
    return robots


def get_positions_after(robots: Set[Robot], width: int, height: int, seconds: int) -> Set[Robot]:
    new_robots = set()
    for robot in robots:
        pos, vel = robot
        new_pos = ((pos[0] + vel[0] * seconds) % width, (pos[1] + vel[1] * seconds) % height)
        new_robots.add((new_pos, vel))
    return new_robots


def count_robots_per_quadrant(robots: Set[Robot], width: int, height: int) -> int:
    quadrants_bounds = {
        1: (0, width // 2 - 1, 0, height // 2 - 1),
        2: (width // 2 + 1, width - 1, 0, height // 2 - 1),
        3: (0, width // 2 - 1, height // 2 + 1, height - 1),
        4: (width // 2 + 1, width - 1, height // 2 + 1, height - 1),
    }
    quadrant_counts = defaultdict(int)
    for robot in robots:
        pos, _ = robot
        for quadrant, bounds in quadrants_bounds.items():
            if bounds[0] <= pos[0] <= bounds[1] and bounds[2] <= pos[1] <= bounds[3]:
                quadrant_counts[quadrant] += 1
                break
    return prod(quadrant_counts.values())


def print_map(robots: Set[Robot], width: int, height: int) -> None:
    current_map = Counter(pos for pos, _ in robots)
    for y in range(height):
        row = "".join(str(current_map.get((x, y), ".")).replace("0", ".") for x in range(width))
        print(row)


def part_A(input_filename: str, width: int, height: int) -> int:
    robots = read_input(input_filename)
    robots_after = get_positions_after(robots, width, height, 100)
    # print_map(robots_after, width, height)
    return count_robots_per_quadrant(robots_after, width, height)


def is_all_different(robots: Set[Robot]) -> bool:
    return len({pos for pos, _ in robots}) == len(robots)


def save_robots_as_png(robots: Set[Robot], width: int, height: int, filename: str) -> None:
    from PIL import Image

    # Create a new black image
    img = Image.new("RGB", (width, height), color="black")
    pixels = img.load()
    if pixels is None:
        raise RuntimeError("Failed to load image pixels")

    # Set white pixels where robots are
    for pos, _ in robots:
        x, y = pos
        if 0 <= x < width and 0 <= y < height:
            pixels[x, y] = (255, 255, 255)  # White

    # Save the image
    img.save(filename)


def part_B(input_filename: str, width: int, height: int) -> int:
    robots = read_input(input_filename)
    # I know that at 1169 seconds the robots are in distinct positions, but without displaying a tree.
    seconds = 1170
    robots = get_positions_after(robots, width, height, seconds)
    while not is_all_different(robots):
        seconds += 1
        robots = get_positions_after(robots, width, height, 1)
    # print_map(robots, width, height)
    # save_robots_as_png(robots, width, height, "day_14.png")
    return seconds


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample.txt"
    # width, height = 11, 7
    input_filename = f"day_{DAY}_input.txt"
    width, height = 101, 103

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename, width, height)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename, width=width, height=height)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
