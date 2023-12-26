from day_24_part_A import DAY, part_A
from day_24_part_B import part_B


def test_part_A():
    assert part_A(f"day_{DAY}_input_sample.txt", ((7, 7), (27, 27))) == 2


def test_part_B():
    assert part_B(f"day_{DAY}_input_sample.txt") == 47
