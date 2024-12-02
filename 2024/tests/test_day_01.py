from day_01 import part_A, part_B


def test_part_A() -> None:
    assert part_A("day_01_input_sample.txt") == 11
    assert part_A("day_01_input.txt") == 1970720


def test_part_B() -> None:
    assert part_B("day_01_input_sample.txt") == 31
    assert part_B("day_01_input.txt") == 17191599
