"""
Advent of Code 2024
--- Day 23: LAN Party ---
https://adventofcode.com/2024/day/23

"""

from collections import Counter
from typing import Any, Dict, List, Set

from aoc_performance import aoc_perf

DAY = "23"


def read_input(input_filename: str) -> Any:
    connections: Dict[str, List[str]] = {}
    with open(input_filename, "r") as file:
        for line in file.read().splitlines():
            source, target = line.split("-")
            connections.setdefault(source, []).append(target)
            connections.setdefault(target, []).append(source)
    return connections


def count_three_connections(connections: Dict[str, List[str]], starts_with: str = "") -> int:
    inter_connected: Set = set()
    for src, targets in connections.items():
        if not src.startswith(starts_with):
            continue
        counter1 = Counter(targets)
        for t in targets:
            counter2 = Counter(connections[t])
            common_elements = counter1 & counter2
            for k in common_elements:
                inter = tuple(sorted([src, t, k]))
                inter_connected.add(inter)
    return len(inter_connected)


def get_sub_networks(connections: Dict[str, List[str]]) -> int:
    # inter_connected: Set = set()
    # for src, targets in connections.items():
    #     network = [src, *targets]
    #     counter1 = Counter(network)
    #     for t in targets:
    #         network2 = [t, *connections[t]]
    #         counter2 = Counter(network2)
    #         common_elements = counter1 & counter2
    #     inter = tuple(sorted(common_elements))
    #     inter_connected.add(inter)
    # return inter_connected
    ...


def part_A(input_filename: str) -> int:
    connections = read_input(input_filename)
    return count_three_connections(connections, "t")


def part_B(input_filename: str) -> int:
    connections = read_input(input_filename)
    sub_networks = get_sub_networks(connections)
    return 0


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    # input_filename = f"day_{DAY}_input.txt"

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
