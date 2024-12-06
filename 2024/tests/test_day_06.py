from day_06 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 41
    assert part_A(f"day_{DAY}_input.txt") == 4696


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 6
    # assert part_B(f"day_{DAY}_input.txt") == 41
