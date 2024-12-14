from day_14 import part_A, part_B, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt", 11, 7) == 12
    assert part_A(f"day_{DAY}_input.txt", 101, 103) == 231019008


# def test_part_B() -> None:
#     assert part_B(f"day_{DAY}_input.txt", 101, 103) == 8280
