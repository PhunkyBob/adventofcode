import pytest
import sys

sys.path.append("..")
from day_22_AB import Map

DAY = "22"

INPUT_SAMPLE = f"day_{DAY}_input_sample.txt"
INPUT = f"day_{DAY}_input.txt"


def test_init():
    map = Map(INPUT_SAMPLE)
    assert map.map_width == 16
    assert map.map_height == 12
    assert (10, 0) in map.open_tiles
    assert (11, 0) in map.walls


def test_move_open():
    map = Map(INPUT_SAMPLE)
    map.position = (9, 0)
    new_x, new_y = map.get_next_position(map.position, "R")
    assert (new_x, new_y) == (10, 0)


def test_move_wall():
    map = Map(INPUT_SAMPLE)
    map.position = (10, 0)
    new_x, new_y = map.get_next_position(map.position, "R")
    assert (new_x, new_y) == (10, 0)


def test_move_wrap_horizontal():
    map = Map(INPUT_SAMPLE)
    map.position = (11, 1)
    new_x, new_y = map.get_next_position(map.position, "R")
    assert (new_x, new_y) == (8, 1)
    map.position = (8, 1)
    new_x, new_y = map.get_next_position(map.position, "L")
    assert (new_x, new_y) == (11, 1)


def test_move_wrap_vertical():
    map = Map(INPUT_SAMPLE)
    map.position = (8, 0)
    new_x, new_y = map.get_next_position(map.position, "U")
    assert (new_x, new_y) == (8, 11)
    map.position = (8, 11)
    new_x, new_y = map.get_next_position(map.position, "D")
    assert (new_x, new_y) == (8, 0)


if __name__ == "__main__":
    pass
