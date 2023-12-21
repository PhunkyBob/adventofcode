"""
Advent of Code 2023

https://adventofcode.com/2023/day/21

"""
from typing import Any, Callable, List, Dict, Tuple
from aoc_performance import aoc_perf

DAY = "21"

Cell = Tuple[int, int]

directions: Dict[str, Cell] = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}


def read_input(input_filename: str) -> Tuple[List[Cell], Cell, Tuple[Cell, Cell]]:  # rocks, start, bounds
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()
        start_pos = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line.strip()) if c == "S"][0]
        return (
            [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line.strip()) if c == "#"],
            start_pos,
            ((0, 0), (len(lines[0].strip()) - 1, len(lines) - 1)),
        )


def calc_min_distances(
    rocks: List[Cell], start: Cell, bounds: Tuple[Cell, Cell], max_distance: int = 64
) -> Dict[Cell, int]:
    min_distances: Dict[Cell, int] = {start: 0}
    to_visit: List[Cell] = [start]
    while to_visit:
        current = to_visit.pop(0)
        for direction in directions.values():
            next_pos = (current[0] + direction[0], current[1] + direction[1])
            mod_x = next_pos[0] % bounds[1][0]
            mod_y = next_pos[1] % bounds[1][1]
            if (
                (mod_x, mod_y) not in rocks
                and next_pos not in min_distances
                and min_distances[current] + 1 <= max_distance
                # and bounds[0][0] <= next_pos[0] <= bounds[1][0]
                # and bounds[0][1] <= next_pos[1] <= bounds[1][1]
            ):
                min_distances[next_pos] = min_distances[current] + 1
                to_visit.append(next_pos)
    return min_distances


def count_reachable(min_distances: Dict[Cell, int], start: Cell, max_distance: int = 64) -> int:
    reachable = 0
    for pos, distance in min_distances.items():
        oddity = ((pos[0] - start[0]) % 2 + (pos[1] - start[1]) % 2) % 2 == max_distance % 2
        if distance <= max_distance and oddity:
            reachable += 1
    return reachable


def display(rocks: List[Cell], start: Cell, bounds: Tuple[Cell, Cell], min_distances: Dict[Cell, int]) -> None:
    min_x, min_y = min(x for x, y in min_distances), min(y for x, y in min_distances)
    max_x, max_y = max(x for x, y in min_distances), max(y for x, y in min_distances)
    output = ""
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            mod_x = x % bounds[1][0]
            mod_y = y % bounds[1][1]
            if (x, y) == start:
                output += "S"
            elif (mod_x, mod_y) in rocks:
                output += "#"
            elif (x, y) in min_distances:
                output += "O"
            else:
                output += "."
        output += "\n"
    with open("output.txt", "w") as output_file:
        output_file.write(output)


def part_A(input_filename: str, distance: int = 64) -> int:
    # distance = 128
    rocks, start, bounds = read_input(input_filename)
    min_distances = calc_min_distances(rocks, start, bounds, distance)
    # display(rocks, start, bounds, min_distances)
    return count_reachable(min_distances, start, distance)


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected answer: 3637

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
