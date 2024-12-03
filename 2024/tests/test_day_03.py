from day_03 import part_A, part_B


def test_part_A() -> None:
    assert part_A("day_03_input_sample_A.txt") == 161
    assert part_A("day_03_input.txt") == 184122457


def test_part_B() -> None:
    assert part_B("day_03_input_sample_B.txt") == 48
    assert part_B("day_03_input.txt") == 107862689
