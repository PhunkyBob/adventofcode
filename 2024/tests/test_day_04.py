from day_04 import DAY, part_A, part_B


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 18
    assert part_A(f"day_{DAY}_input.txt") == 2536


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 9
    assert part_B(f"day_{DAY}_input.txt") == 1875
