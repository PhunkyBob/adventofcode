"""
Advent of Code 2024
--- Day 9: Disk Fragmenter ---
https://adventofcode.com/2024/day/9

2333133121414131402

00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............
"""

from dataclasses import dataclass
from itertools import batched
from typing import Any, Callable, Dict, List, Optional, Tuple

from aoc_performance import aoc_perf

DAY = "09"


def read_input(input_filename: str) -> str:
    with open(input_filename, "r") as file:
        data = file.read().strip()
    return data


def create_map(data: str) -> Tuple[List[Optional[int]], List[int]]:
    drive_map: List[Optional[int]] = []
    free_space: List[int] = []
    id_number = 0
    position = 0
    for item in batched(data, 2):
        file_size = int(item[0])
        for _ in range(file_size):
            drive_map.append(id_number)
            position += 1
        if len(item) == 2:
            blank_size = int(item[1])
            for _ in range(blank_size):
                drive_map.append(None)
                free_space.append(position)
                position += 1
        id_number += 1
    return drive_map, free_space


def defrag_A(drive_map: List[Optional[int]], free_space: List[int]) -> List[Optional[int]]:
    for i in range(len(drive_map) - 1, 0, -1):
        if len(free_space) == 0 or free_space[0] > i:
            break
        if drive_map[i] is not None:
            drive_map[free_space.pop(0)] = drive_map[i]
            drive_map[i] = None
    return drive_map


def get_checksum(drive_map: List[Optional[int]]) -> int:
    checksum = 0
    for i in range(len(drive_map)):
        if drive_map[i] is None:
            break
        checksum += drive_map[i] * i
    return checksum


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    drive_map, free_state = create_map(data)
    drive_map = defrag_A(drive_map, free_state)
    return get_checksum(drive_map)


@dataclass
class Node:
    id: int | None = None
    length: int = 0


def create_map_as_nodes(data: str) -> List[Node]:
    drive_map: List[Node] = []
    id_number = 0
    for item in batched(data, 2):
        file_size = int(item[0])
        drive_map.append(Node(id_number, file_size))
        if len(item) == 2:
            blank_size = int(item[1])
            drive_map.append(Node(None, blank_size))
        id_number += 1
    return drive_map


def find_empty_space(drive_map: List[Node], size: int) -> int:
    for i in range(len(drive_map)):
        if drive_map[i].id is None and drive_map[i].length >= size:
            return i
    return -1


def defrag_B(drive_map: List[Node]) -> List[Node]:
    node_id = len(drive_map) - 1
    while node_id > 0:
        if drive_map[node_id].id is not None:
            new_position = find_empty_space(drive_map, drive_map[node_id].length)
            if new_position >= 0:

                drive_map[new_position].id = drive_map[node_id].id
                drive_map[new_position + 1].length -= drive_map[node_id].length
                drive_map[node_id].id = None
                drive_map[node_id].length = 0

    return drive_map


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    drive_map = create_map_as_nodes(data)

    return 0


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
