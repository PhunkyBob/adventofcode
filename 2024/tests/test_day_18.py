from day_18 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt", 7, 12) == 22
    assert part_A(f"day_{DAY}_input.txt", 71, 1024) == 354


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt", 7, 12) == "6,1"
    assert part_B(f"day_{DAY}_input.txt", 71, 1024) == "36,17"
