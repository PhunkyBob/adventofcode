"""
Advent of Code 2023

https://adventofcode.com/2023/day/25

"""

from functools import reduce
from operator import mul
from typing import Any, Callable, Dict, List, Tuple

import networkx as nx

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "25"


Edge = Tuple[str, str]


def read_input(input_filename: str) -> List[Edge]:
    edges: List[Edge] = []
    with open(input_filename, "r") as f:
        for line in f:
            left, right = line.strip().split(":")
            edges.extend((left.strip(), elem.strip()) for elem in right.strip().split(" "))
    return edges


def edges_to_remove_to_disconnect(graph):
    return list(nx.stoer_wagner(graph))


def part_A(input_filename: str) -> int:
    edges = read_input(input_filename)
    # Exemple de création d'un graphe et recherche des arêtes à supprimer
    G = nx.Graph()
    G.add_edges_from(edges)
    edges_to_remove = edges_to_remove_to_disconnect(G)
    return reduce(lambda x, y: x * len(y), edges_to_remove[1], 1)


def main() -> None:
    download_input(DAY, 2023)
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
