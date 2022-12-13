import pytest
import sys

sys.path.append("..")
from day_13_AB import DistressSignal

DAY = "13"

INPUT_SAMPLE = f"day_{DAY}_input_sample.txt"
INPUT = f"day_{DAY}_input.txt"


def test_init_packet():
    data = DistressSignal(INPUT_SAMPLE)
    assert data.pairs[-1].right == [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]


def test_compare_packet():
    data = DistressSignal(INPUT_SAMPLE)


if __name__ == "__main__":
    pass
