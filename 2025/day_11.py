"""
Advent of Code 2025

https://adventofcode.com/2025/day/11

"""

from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "11"


def read_input(input_filename: str) -> Dict[str, List[str]]:
    data: Dict[str, List[str]] = {}
    with open(input_filename, "r") as file:
        for line in file.read().splitlines():
            key, values_txt = line.split(": ")
            values = values_txt.strip().split(" ")
            data[key] = values
    data["out"] = []
    return data


def get_possible_paths(data, from_node: str = "you", to_node: str = "out") -> List[List[str]]:
    queue: List[List[str]] = [[from_node]]
    possible_paths: List[List[str]] = []
    while queue:
        path = queue.pop(0)
        current_node = path[-1]
        for neighbor in data.get(current_node, []):
            if neighbor == to_node:
                possible_paths.append(path + [neighbor])
                continue
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append(new_path)
    return possible_paths


def part_A(input_filename: str) -> int:
    graph = read_input(input_filename)
    return len(get_possible_paths(graph))


def part_B(input_filename: str) -> int:
    graph = read_input(input_filename)
    mandatory = {"fft": 0, "dac": 1}
    memo = {}

    def count_paths(node, mask):
        if node == "out":
            return 1 if mask == 3 else 0  # Valide seulement si les deux bits sont à 1

        key = (node, mask)
        if key in memo:
            return memo[key]

        # Mettre à jour le masque si le nœud courant est obligatoire
        new_mask = mask
        if node in mandatory:
            new_mask |= 1 << mandatory[node]

        res = 0
        for child in graph.get(node, []):
            res += count_paths(child, new_mask)

        memo[key] = res
        return res

    return count_paths("svr", 0)


def main() -> None:
    download_input(DAY, 2025)
    # input_filename = f"day_{DAY}_input_sample.txt"
    # input_filename = f"day_{DAY}_input_sample2.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Answer: 708

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Answer: 545394698933400


if __name__ == "__main__":
    main()
