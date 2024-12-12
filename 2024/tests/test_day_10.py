from day_10 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample1.txt") == 2
    assert part_A(f"day_{DAY}_input_sample2.txt") == 4
    assert part_A(f"day_{DAY}_input_sample3.txt") == 36
    assert part_A(f"day_{DAY}_input.txt") == 822


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample1.txt") == 2
    assert part_B(f"day_{DAY}_input_sample2.txt") == 13
    assert part_B(f"day_{DAY}_input_sample3.txt") == 81
    assert part_B(f"day_{DAY}_input.txt") == 1801
