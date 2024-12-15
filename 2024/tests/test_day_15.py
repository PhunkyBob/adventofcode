from day_15_part_A import part_A, DAY
from day_15_part_B import part_B


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample1.txt") == 2028
    assert part_A(f"day_{DAY}_input_sample2.txt") == 10092
    assert part_A(f"day_{DAY}_input.txt") == 1360570


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample2.txt") == 9021
    assert part_B(f"day_{DAY}_input.txt") == 1381446
