import pytest
import sys

sys.path.append("..")
from day_13_AB import DistressSignal

DAY = "13"

INPUT_SAMPLE = f"day_{DAY}_input_sample.txt"
INPUT = f"day_{DAY}_input.txt"


def test_init_packet():
    data = DistressSignal(INPUT_SAMPLE)
    assert data.items[-1] == [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]


def test_compare_packet():
    data = DistressSignal(INPUT_SAMPLE, True)
    res = data.is_right_order(0)
    assert res == True

    res = data.is_right_order(1)
    assert res == True

    res = data.is_right_order(2)
    assert res == False

    res = data.is_right_order(3)
    assert res == True

    res = data.is_right_order(4)
    assert res == False

    res = data.is_right_order(5)
    assert res == True

    res = data.is_right_order(6)
    assert res == False

    res = data.is_right_order(7)
    assert res == False


def test_compare_indiv():
    data = DistressSignal(INPUT_SAMPLE, True)
    res = DistressSignal.is_smaller(data.items[0], data.items[4], debug=True)
    assert res == False


if __name__ == "__main__":
    test_compare_packet()
