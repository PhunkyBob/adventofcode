from day_13 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 480
    assert part_A(f"day_{DAY}_input.txt") == 31589


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 875318608908
    assert part_B(f"day_{DAY}_input.txt") == 98080815200063
