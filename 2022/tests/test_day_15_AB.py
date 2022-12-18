import pytest
import sys

sys.path.append("..")
from day_15_AB import Map

DAY = "15"

INPUT_SAMPLE = f"day_{DAY}_input_sample.txt"
INPUT = f"day_{DAY}_input.txt"


def test_manhattan():
    dist = Map.manhattan_distance(2, 18, -2, 15)
    assert dist == 7


def test_init():
    map = Map(INPUT_SAMPLE)
    assert len(map.sensors) == 14
    assert len(map.beacons) == 6


if __name__ == "__main__":
    pass
