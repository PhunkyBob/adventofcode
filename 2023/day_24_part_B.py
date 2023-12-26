"""
Advent of Code 2023

https://adventofcode.com/2023/day/24

"""
import itertools
from typing import Any, Callable, List, Dict, Optional, Tuple
from aoc_performance import aoc_perf
import re
import z3
from z3 import ExprRef

DAY = "24"

Point3D = Tuple[int, int, int]  # x, y, z
Vector3D = Tuple[int, int, int]  # x, y, z
Line3D = Tuple[Point3D, Vector3D]
Intersection = Tuple[Optional[float], Optional[float]]


def read_input(input_filename: str) -> List[Line3D]:
    lines = []
    with open(input_filename, "r") as f:
        for line in f:
            if res := re.match(r"(\d+), (\d+), (\d+) @ ([-\d]+),\s*([-\d]+),\s*([-\d]+)", line.strip()):
                x, y, z, vx, vy, vz = map(int, res.groups())
                point = (x, y, z)
                vector = (vx, vy, vz)
                lines.append((point, vector))
    return lines


def part_B(input_filename: str) -> int:
    lines = read_input(input_filename)

    rock_x, rock_y, rock_z, vec_x, vec_y, vec_z = z3.Ints("rock_x rock_y rock_z vec_x vec_y vec_z")
    times = [z3.Int(f"time_{str(i)}") for i in range(len(lines))]

    s = z3.Solver()
    for i, ((pos_x, pos_y, pos_z), (v_x, v_y, v_z)) in enumerate(lines):
        s.add(pos_x + v_x * times[i] == rock_x + vec_x * times[i])
        s.add(pos_y + v_y * times[i] == rock_y + vec_y * times[i])
        s.add(pos_z + v_z * times[i] == rock_z + vec_z * times[i])
    s.check()
    res: ExprRef = s.model().eval(rock_x + rock_y + rock_z)
    return res.as_long() // 1


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
