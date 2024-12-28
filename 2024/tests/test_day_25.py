from day_25 import part_A, DAY, read_input
import numpy as np


def test_read_input() -> None:
    locks, keys = read_input(f"day_{DAY}_input_sample.txt")
    assert np.array_equal(locks, [[0, 5, 3, 4, 3], [1, 2, 0, 5, 3]])
    assert np.array_equal(keys, [[5, 0, 2, 1, 3], [4, 3, 4, 0, 2], [3, 0, 2, 0, 1]])


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 3
    assert part_A(f"day_{DAY}_input.txt") == 3690
