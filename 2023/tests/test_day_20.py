from day_20 import DAY, part_A, part_B


def test_part_A():
    assert part_A(f"day_{DAY}_input_sample.txt") == 32000000
    assert part_A(f"day_{DAY}_input_sample2.txt") == 11687500
