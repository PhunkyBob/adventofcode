from day_07 import part_A, part_B, DAY, is_possibly_true_B


def test_is_possibly_true() -> None:
    result, items = 190, [10, 19]
    assert is_possibly_true_B(result, 0, items) == True
    result, items = 3267, [81, 40, 27]
    assert is_possibly_true_B(result, 0, items) == True
    result, items = 83, [17, 5]
    assert is_possibly_true_B(result, 0, items) == False
    result, items = 292, [11, 6, 16, 20]
    assert is_possibly_true_B(result, 0, items) == True


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 3749
    assert part_A(f"day_{DAY}_input.txt") == 2299996598890


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 11387
    # assert part_B(f"day_{DAY}_input.txt") == 362646859298554
