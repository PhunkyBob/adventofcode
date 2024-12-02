from day_02 import part_A, part_B


def test_part_A() -> None:
    assert part_A("day_02_input_sample.txt") == 2
    assert part_A("day_02_input.txt") == 591


def test_part_B() -> None:
    assert part_B("day_02_input_sample.txt") == 4
    assert part_B("day_02_input.txt") == 621
