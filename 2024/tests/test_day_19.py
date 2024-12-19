from day_19 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 6
    assert part_A(f"day_{DAY}_input.txt") == 300


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 16
    assert part_B(f"day_{DAY}_input.txt") == 624802218898092
