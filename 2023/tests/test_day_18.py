from day_18 import DAY, part_A, part_B


def test_part_A():
    assert part_A(f"day_{DAY}_input_sample.txt") == 62


def test_part_B():
    assert part_B(f"day_{DAY}_input_sample.txt") == 952408144115
