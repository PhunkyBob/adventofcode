from day_09 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 1928
    assert part_A(f"day_{DAY}_input.txt") == 6334655979668


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 2858
    # assert part_B(f"day_{DAY}_input.txt") == 6349492251099
