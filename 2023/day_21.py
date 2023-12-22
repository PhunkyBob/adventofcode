"""
Advent of Code 2023
--- Day 21: Step Counter ---
https://adventofcode.com/2023/day/21

The Elf starts at the starting position (S) which also counts as a garden plot. Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots. This would allow him to reach any of the tiles marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

"""
import heapq
from typing import  List, Dict, Set, Tuple
from aoc_performance import aoc_perf

DAY = "21"

Cell = Tuple[int, int]

directions: Dict[str, Cell] = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}


def read_input(input_filename: str) -> Tuple[Set[Cell], Cell, Tuple[Cell, Cell]]:  # rocks, start, bounds
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()
        start_pos = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line.strip()) if c == "S"][0]
        return (
            {(x, y) for y, line in enumerate(lines) for x, c in enumerate(line.strip()) if c == "#"},
            start_pos,
            ((0, 0), (len(lines[0].strip()) - 1, len(lines) - 1)),
        )


def calc_min_distances(
    rocks: Set[Cell], start: Cell, bounds: Tuple[Cell, Cell], max_distance: int = 64
) -> Dict[Cell, int]:
    min_distances: Dict[Cell, int] = {start: 0}
    to_visit: List[Cell] = []
    heapq.heappush(to_visit, start)
    while to_visit:
        current = heapq.heappop(to_visit)
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
                heapq.heappush(to_visit, next_pos)
    return min_distances


def count_reachable(min_distances: Dict[Cell, int], start: Cell, max_distance: int = 64) -> int:
    reachable = 0
    for pos, distance in min_distances.items():
        oddity = (pos[0] - start[0] + pos[1] - start[1]) % 2 == max_distance % 2
        if distance <= max_distance and oddity:
            reachable += 1
    return reachable


def display(rocks: Set[Cell], start: Cell, bounds: Tuple[Cell, Cell], min_distances: Dict[Cell, int]) -> None:
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
    # distance = 64 + 131 * 2
    rocks, start, bounds = read_input(input_filename)
    min_distances = calc_min_distances(rocks, start, bounds, distance)
    # display(rocks, start, bounds, min_distances)
    return count_reachable(min_distances, start, distance)


def count_reachable_2(rocks: Set[Cell], start: Cell, square_width, max_distance: int = 64) -> int:
    # def count_reachable_2(world_of_rocks: List[List[bool]], start: Cell, square_width, max_distance: int = 64) -> int:
    """Assuming that the pattern is a square."""
    visited: Set[Cell] = set()
    to_visit: List[Tuple[int, Cell]] = []  # (steps, pos)
    heapq.heapify(to_visit)
    heapq.heappush(to_visit, (0, start))
    current_step = previous_step = 0
    cycles = []
    while to_visit:
        current_step, current = heapq.heappop(to_visit)
        if current in visited:
            continue
        visited.add(current)
        if current_step != previous_step:
            # It's the last step of the cycle
            # print(f"Step {previous_step} : queue {len(to_visit)}, seen {len(visited)}")
            if previous_step % (square_width * 2) == max_distance % (square_width * 2):
                cycles.append(sum((x + y) % 2 == 1 for (x, y) in visited))
                if len(cycles) == 3:
                    # print(cycles)
                    answer, offset, increment = (
                        cycles[0],
                        cycles[1] - cycles[0],
                        (cycles[2] - cycles[1]) - (cycles[1] - cycles[0]),
                    )
                    for _ in range(max_distance // (square_width * 2)):
                        answer += offset
                        offset += increment
                    return answer

        for next_pos in (
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1]),
            (current[0], current[1] + 1),
            (current[0], current[1] - 1),
        ):
            if (next_pos[0] % square_width, next_pos[1] % square_width) not in rocks and next_pos not in visited:
                heapq.heappush(to_visit, (current_step + 1, next_pos))
        previous_step = current_step
    raise Exception("No answer found")


def part_B(input_filename: str) -> int:
    # 26501365 = 202300 * 131 + 65
    # 65 -> 3699
    # 65 + 131 * 2 = 327 -> 91951
    # 65 + 131 * 4 = 589 -> 297707
    rocks, start, bounds = read_input(input_filename)
    return count_reachable_2(rocks, start, bounds[1][0] + 1, 26501365)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected answer: 3637

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected answer: 601113643448699


if __name__ == "__main__":
    main()
