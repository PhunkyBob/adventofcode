"""
Advent of Code 2023
--- Day 17: Clumsy Crucible ---
https://adventofcode.com/2023/day/17

Vizualisation of the solution of day 17.
"""
from enum import Enum
from typing import Any, Callable, List, Dict, NamedTuple, Optional, Set, Tuple
from aoc_performance import aoc_perf
import heapq


from dataclasses import dataclass
import pygame
import random

pygame.font.init()

DAY = "17"


Direction = Tuple[int, int]
Coord = Tuple[int, int]
Element = Tuple[Coord, Direction, int]
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT_SIZE = 6
FONT = pygame.font.SysFont("Arial", 18)
CLOCK = None

FPS = 120
VEL = 5


COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)


def read_input(filename: str) -> List[List[int]]:
    with open(filename, "r") as f:
        return [list(map(int, list(line.strip()))) for line in f.readlines()]


def find_shortest_path(
    matrix: List[List[int]],
    max_direction_count: int = 3,
    min_direction_count: int = 1,
    start: Coord = (0, 0),
    end: Optional[Coord] = None,
):
    if end is None:
        end = (len(matrix[0]) - 1, len(matrix) - 1)
    candidates: List[Tuple[int, Element]] = []
    for dir in [UP, RIGHT, DOWN, LEFT]:
        heapq.heappush(candidates, (0, (start, dir, 1)))
    certains: Set[Element] = set()
    iteration = 0
    while candidates:
        iteration += 1
        if iteration % 100_000 == 0:
            print(f"Iteration {iteration}")
        cost, current = heapq.heappop(candidates)
        if current in certains:
            continue
        certains.add(current)
        new_coord = (current[0][0] + current[1][0], current[0][1] + current[1][1])
        if new_coord[0] < 0 or new_coord[0] >= len(matrix[0]) or new_coord[1] < 0 or new_coord[1] >= len(matrix):
            continue
        new_cost = cost + matrix[new_coord[1]][new_coord[0]]
        if min_direction_count <= current[2] <= max_direction_count and new_coord == end:
            yield None, None
        for new_direction in [UP, RIGHT, DOWN, LEFT]:
            if new_direction[0] == 0 - current[1][0] and new_direction[1] == 0 - current[1][1]:
                continue
            new_direction_count = current[2] + 1 if new_direction == current[1] else 1
            if new_direction_count > max_direction_count or (
                current[1] != new_direction and current[2] < min_direction_count
            ):
                continue
            if (new_coord, new_direction, new_direction_count) not in certains:
                heapq.heappush(candidates, (new_cost, (new_coord, new_direction, new_direction_count)))
        yield candidates, certains
    return None, None


def init_window(matrix: List[List[int]]) -> None:
    global WIN, FONT, CLOCK, WIDTH, HEIGHT, FONT_SIZE

    # FONT_SIZE = 9
    WIDTH, HEIGHT = len(matrix[0]) * FONT_SIZE, len(matrix) * FONT_SIZE
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("AoC 2023 - Day 17 - Clumsy Crucible")

    FONT = pygame.font.SysFont("Arial", FONT_SIZE)
    CLOCK = pygame.time.Clock()
    WIN.fill(COLOR_BLACK)
    draw_matrix(matrix)


def fps_counter():
    fps = f"{int(CLOCK.get_fps())} fps"
    fps_t = FONT.render(fps, 1, pygame.Color("WHITE"))
    WIN.blit(fps_t, (10, 10))


def draw_matrix(matrix: List[List[int]]) -> None:
    for y, line in enumerate(matrix):
        for x, value in enumerate(line):
            comp = int(255 / 16 * (16 - value))
            color = (comp, comp, comp)
            pygame.draw.rect(WIN, color, (x * FONT_SIZE, y * FONT_SIZE, FONT_SIZE, FONT_SIZE))


def draw_candidates(candidates: List[Tuple[int, Element]]):
    for candidate in candidates:
        coord = candidate[1][0]
        pygame.draw.rect(WIN, COLOR_YELLOW, (coord[0] * FONT_SIZE, coord[1] * FONT_SIZE, FONT_SIZE, FONT_SIZE))


def draw_certains(certains: Set[Element]):
    for certain in certains:
        coord = certain[0]
        pygame.draw.rect(WIN, COLOR_RED, (coord[0] * FONT_SIZE, coord[1] * FONT_SIZE, FONT_SIZE, FONT_SIZE))


def draw_window(matrix: List[List[int]], candidates: List[Tuple[int, Element]], certains: Set[Element]):
    draw_candidates(candidates)
    draw_certains(certains)
    fps_counter()
    pygame.display.update()


def main():
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"
    matrix = read_input(input_filename)
    init_window(matrix)

    gen = find_shortest_path(matrix)
    run = True
    while run:
        # CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        candidates, certains = next(gen)
        if candidates is None or certains is None:
            run = False
        else:
            draw_window(matrix, candidates, certains)
    pygame.quit()


if __name__ == "__main__":
    main()
