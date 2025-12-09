"""
Advent of Code 2025

https://adventofcode.com/2025/day/8

"""

import heapq
import sys
from functools import lru_cache
from itertools import starmap
from math import sqrt
from typing import Any, Callable, Dict, List, Set, Tuple

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "08"

Coord = tuple[int, int, int]


def read_input(input_filename: str) -> List[Coord]:
    data: List[Coord] = []
    with open(input_filename, "r") as file:
        for line in file.read().splitlines():
            coord: Coord = tuple(int(val) for val in line.split(","))  # pyright: ignore[reportAssignmentType]
            data.append(coord)
    return data


@lru_cache(maxsize=None)
def get_distance(coord1: Coord, coord2: Coord) -> float:
    if coord1 > coord2:
        return get_distance(coord2, coord1)
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def get_all_distances(data: List[Coord]) -> List[Tuple[Coord, Coord, float]]:
    distances: List[Tuple[Coord, Coord, float]] = []
    for coord1 in data:
        for coord2 in data:
            if coord1 < coord2:  # We store each distance only once
                distance = get_distance(coord1, coord2)
                distances.append((coord1, coord2, distance))
    return distances


def part_A(input_filename: str, limit: int = sys.maxsize) -> int:
    data = read_input(input_filename)
    distances = get_all_distances(data)
    heapq.heapify(distances)
    sorted_distances: List[Tuple[Coord, Coord, float]] = heapq.nsmallest(limit, distances, key=lambda dist: dist[2])

    circuits: List[List[Coord]] = []
    while sorted_distances:
        coord1, coord2, _ = sorted_distances.pop(0)
        coord1_is_in_circuit = -1
        coord2_is_in_circuit = -1
        for i, circuit in enumerate(circuits):
            if coord1 in circuit:
                coord1_is_in_circuit = i
            if coord2 in circuit:
                coord2_is_in_circuit = i

        if coord1_is_in_circuit == -1 and coord2_is_in_circuit == -1:
            circuits.append([coord1, coord2])
        elif coord1_is_in_circuit != -1 and coord2_is_in_circuit == -1:
            circuits[coord1_is_in_circuit].append(coord2)
        elif coord1_is_in_circuit == -1 and coord2_is_in_circuit != -1:
            circuits[coord2_is_in_circuit].append(coord1)
        elif coord1_is_in_circuit != -1 and coord2_is_in_circuit != -1:
            # Merge circuits
            if coord1_is_in_circuit != coord2_is_in_circuit:
                circuit1 = circuits[coord1_is_in_circuit]
                circuit2 = circuits[coord2_is_in_circuit]
                circuits[coord1_is_in_circuit] = circuit1 + circuit2
                circuits.pop(coord2_is_in_circuit)

    circuit_lengths: List[int] = sorted([len(circuit) for circuit in circuits])
    total = 1
    for length in circuit_lengths[-3:]:
        total *= length
    return total


def part_B(input_filename: str, limit: int = sys.maxsize) -> int:
    data = read_input(input_filename)
    distances = get_all_distances(data)
    heapq.heapify(distances)
    sorted_distances: List[Tuple[Coord, Coord, float]] = heapq.nsmallest(limit, distances, key=lambda dist: dist[2])
    last_coord1, last_coord2 = [], []

    circuits: List[List[Coord]] = []
    while sorted_distances:
        coord1, coord2, _ = sorted_distances.pop(0)
        coord1_is_in_circuit = -1
        coord2_is_in_circuit = -1
        for i, circuit in enumerate(circuits):
            if coord1 in circuit:
                coord1_is_in_circuit = i
            if coord2 in circuit:
                coord2_is_in_circuit = i

        if coord1_is_in_circuit == -1 and coord2_is_in_circuit == -1:
            circuits.append([coord1, coord2])
        elif coord1_is_in_circuit != -1 and coord2_is_in_circuit == -1:
            circuits[coord1_is_in_circuit].append(coord2)
        elif coord1_is_in_circuit == -1 and coord2_is_in_circuit != -1:
            circuits[coord2_is_in_circuit].append(coord1)
        elif coord1_is_in_circuit != -1 and coord2_is_in_circuit != -1:
            # Merge circuits
            if coord1_is_in_circuit != coord2_is_in_circuit:
                circuit1 = circuits[coord1_is_in_circuit]
                circuit2 = circuits[coord2_is_in_circuit]
                circuits[coord1_is_in_circuit] = circuit1 + circuit2
                circuits.pop(coord2_is_in_circuit)
        if len(circuits) == 1 and (coord1_is_in_circuit != 0 or coord2_is_in_circuit != 0):
            last_coord1, last_coord2 = coord1, coord2

    return last_coord1[0] * last_coord2[0]


def main() -> None:
    download_input(DAY, 2025)
    input_filename, limit = f"day_{DAY}_input_sample.txt", 10
    input_filename, limit = f"day_{DAY}_input.txt", 1000

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename, limit)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
