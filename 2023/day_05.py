"""
Advent of Code 2023
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5


"""

import re
from collections import deque, namedtuple
from typing import Any, Callable, Deque, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "05"
Chunk = namedtuple("Chunk", ["start", "length"])


def part_A(input_filename: str) -> int:
    with open(input_filename, "r") as input_file:
        input_data = input_file.read().splitlines()
    seeds = [int(x) for x in input_data[0].split(":")[-1].split(" ") if x]
    new_destinations: Dict[int, int] = {}
    for line in input_data[1:]:
        if "map" in line:
            print(line)
            new_destinations |= {seed: seed for seed in seeds if seed not in new_destinations}
            seeds = list(new_destinations.values())
            new_destinations = {}
            continue
        if res := re.match(r"(\d+) (\d+) (\d+)", line):
            dest, src, amt = map(int, res.groups())
            for seed in seeds:
                if src <= seed < src + amt:
                    new_destinations[seed] = dest + seed - src
    new_destinations |= {seed: seed for seed in seeds if seed not in new_destinations}
    seeds = list(new_destinations.values())
    return min(seeds)


def part_B(input_filename: str) -> int:
    with open(input_filename, "r") as input_file:
        input_data = input_file.read().splitlines()
    seeds = [int(x) for x in input_data[0].split(":")[-1].split(" ") if x]
    new_destinations: Deque[Chunk] = deque([Chunk(int(x[0]), int(x[1])) for x in zip(seeds[::2], seeds[1::2])])
    chunks: Deque[Chunk] = deque()
    to_process = deque()
    for line in input_data[1:]:
        if "map" in line:
            # print(line)
            to_process += new_destinations
            new_destinations: Deque[Chunk] = deque()
            continue
        if res := re.match(r"(\d+) (\d+) (\d+)", line):
            chunks = to_process.copy()
            to_process = deque()
            dest, src, amt = map(int, res.groups())
            while len(chunks) > 0:
                seed = chunks.popleft()
                if seed.start > src + amt - 1 or seed.start + seed.length - 1 < src:
                    # This chunk is completely outside the range
                    to_process.append(seed)
                    continue
                # Part of this chunk is in the range
                if seed.start < src:
                    # The chunk starts before the range
                    before_range = Chunk(seed.start, src - seed.start)
                    to_process.append(before_range)
                if seed.start + seed.length - 1 > src + amt - 1:
                    # The chunk ends after the range
                    after_range = Chunk(src + amt, seed.start + seed.length - src - amt)
                    to_process.append(after_range)
                inside_range = Chunk(
                    max(seed.start, src) - (src - dest),
                    min(seed.start + seed.length - 1, src + amt - 1) - max(seed.start, src) + 1,
                )
                new_destinations.append(inside_range)
    new_destinations += to_process
    return min(new_destinations, key=lambda x: x.start).start


def main() -> None:
    download_input(DAY, 2023)
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
