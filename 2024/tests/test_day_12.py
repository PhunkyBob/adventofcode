from day_12 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample1.txt") == 140
    assert part_A(f"day_{DAY}_input_sample2.txt") == 1930
    assert part_A(f"day_{DAY}_input.txt") == 1415378


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample1.txt") == 80
    assert part_B(f"day_{DAY}_input_sample2.txt") == 1206
    assert part_B(f"day_{DAY}_input.txt") == 862714
