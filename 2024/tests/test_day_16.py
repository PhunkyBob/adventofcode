from day_16 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample1.txt") == 7036
    assert part_A(f"day_{DAY}_input_sample2.txt") == 11048
    assert part_A(f"day_{DAY}_input.txt") == 92432


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample1.txt") == 45
    assert part_B(f"day_{DAY}_input_sample2.txt") == 64
    # assert part_B(f"day_{DAY}_input.txt") == 458
