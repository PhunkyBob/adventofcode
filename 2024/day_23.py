"""
Advent of Code 2024
--- Day 23: LAN Party ---
https://adventofcode.com/2024/day/23

"""

from collections import Counter, deque
from typing import Any, Dict, List, Set, Tuple

import matplotlib.pyplot as plt
import networkx as nx

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "23"


def read_input(input_filename: str) -> Any:
    connections: Dict[str, List[str]] = {}
    with open(input_filename, "r") as file:
        for line in file.read().splitlines():
            source, target = line.split("-")
            connections.setdefault(source, []).append(target)
            connections.setdefault(target, []).append(source)
    return connections


def get_three_connections(connections: Dict[str, List[str]], starts_with: str = "") -> Set[Tuple[str, ...]]:
    return {
        tuple(sorted([src, t, k]))
        for src, targets in connections.items()
        if src.startswith(starts_with)
        for t in targets
        for k in set(targets) & set(connections[t])
    }


def plot_connections(connections: Dict[str, List[str]]) -> None:
    g = nx.Graph()
    for node, links in connections.items():
        for link in links:
            if node < link:
                g.add_edge(node, link)
    plt.figure(figsize=(32, 24))
    nx.draw(g, with_labels=True)
    plt.savefig("day_23.svg", bbox_inches="tight", dpi=300)
    # plt.show()


def part_A(input_filename: str) -> int:
    connections = read_input(input_filename)
    return len(get_three_connections(connections, "t"))


def all_have_x(connections: Dict[str, List[str]], items: Tuple[str, ...], x: str) -> bool:
    return all(x in connections[item] for item in items)


def x_have_all(connections: Dict[str, List[str]], items: Tuple[str, ...], x: str) -> bool:
    return all(item in connections[x] for item in items)


def part_B(input_filename: str) -> str:
    connections = read_input(input_filename)
    starts = get_three_connections(connections, "")
    queue = deque(list(starts))
    longest = 0
    answer = ""
    already_seen = set()
    while queue:
        elem = queue.pop()
        if elem in already_seen:
            continue
        already_seen.add(elem)
        for new_element in connections[elem[0]]:
            if all_have_x(connections, elem, new_element) and x_have_all(connections, elem, new_element):
                new_start = tuple(sorted([new_element, *elem]))
                if new_start not in already_seen:
                    queue.append(new_start)
                if len(new_start) > longest:
                    longest = len(new_start)
                    answer = new_start
    return ",".join(list(answer))


def main() -> None:
    download_input(DAY, 2024)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    # plot_connections(read_input(input_filename))

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
