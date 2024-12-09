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
from collections import namedtuple
from aoc_performance import aoc_perf

DAY = "09"


def read_input(input_filename: str) -> str:
    with open(input_filename, "r") as file:
        data = file.read().strip()
    return data


def create_map_A(data: str) -> Tuple[List[Optional[int]], List[int]]:
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
        if not free_space or free_space[0] > i:
            break
        if drive_map[i] is not None:
            drive_map[free_space.pop(0)] = drive_map[i]
            drive_map[i] = None
    return drive_map


def get_checksum_A(drive_map: List[Optional[int]]) -> int:
    checksum = 0
    for i in range(len(drive_map)):
        if drive_map[i] is None:
            break
        checksum += drive_map[i] * i
    return checksum


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    drive_map, free_state = create_map_A(data)
    drive_map = defrag_A(drive_map, free_state)
    return get_checksum_A(drive_map)


Node = namedtuple("Node", ["id", "length"])


def create_map_as_nodes(data: str) -> List[Node]:
    drive_map: List[Node] = []
    for id_number, item in enumerate(batched(data, 2)):
        file_size = int(item[0])
        drive_map.append(Node(id_number, file_size))
        if len(item) == 2:
            blank_size = int(item[1])
            drive_map.append(Node(None, blank_size))
    return drive_map


def find_empty_space(drive_map: List[Node], size: int) -> int:
    return next(
        (i for i in range(len(drive_map)) if drive_map[i].id is None and drive_map[i].length >= size),
        -1,
    )


def print_drive_map_B(drive_map: List[Node]) -> None:
    for node in drive_map:
        element = "." if node.id is None else str(node.id)
        print(element * node.length, end="")
    print()


def defrag_B(drive_map: List[Node]) -> List[Node]:
    node_id = len(drive_map) - 1
    while node_id > 0:
        # print_drive_map_B(drive_map)
        if drive_map[node_id].id is not None:
            new_position = find_empty_space(drive_map, drive_map[node_id].length)
            if new_position >= 0 and new_position < node_id:
                empty_node: Node = Node(None, drive_map[new_position].length - drive_map[node_id].length)
                current_node: Node = drive_map[node_id]
                drive_map[new_position : new_position + 1] = [current_node, empty_node]
                drive_map[node_id + 1] = Node(None, current_node.length)
            else:
                node_id -= 1
        else:
            node_id -= 1

    return drive_map


def get_checksum_B(drive_map: List[Node]) -> int:
    checksum = 0
    index = 0
    for node in drive_map:
        for _ in range(node.length):
            if node.id is not None:
                checksum += node.id * index
            index += 1
    return checksum


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    drive_map = create_map_as_nodes(data)
    drive_map = defrag_B(drive_map)
    return get_checksum_B(drive_map)


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
