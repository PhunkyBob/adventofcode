from day_22 import DAY, part_A, part_B


def test_part_A():
    assert part_A(f"day_{DAY}_input_sample.txt") == 5


def test_part_B():
    assert part_B(f"day_{DAY}_input_sample.txt") == 7
