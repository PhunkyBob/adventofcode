from day_11 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 55312
    assert part_A(f"day_{DAY}_input.txt") == 189167


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 65601038650482
    assert part_B(f"day_{DAY}_input.txt") == 225253278506288
