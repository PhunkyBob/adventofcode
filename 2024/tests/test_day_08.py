from day_08 import part_A, part_B, DAY, get_antinodes_B


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 14
    assert part_A(f"day_{DAY}_input.txt") == 392


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 34
    assert part_B(f"day_{DAY}_input.txt") == 1235
