from day_24 import part_A, DAY


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 2024
    assert part_A(f"day_{DAY}_input.txt") == 45213383376616
