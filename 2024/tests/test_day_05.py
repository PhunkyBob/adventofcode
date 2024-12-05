from day_05 import DAY, get_middle_element, part_A, part_B, reorder_update, is_sorted

successors = {
    47: [53, 13, 61, 29],
    97: [13, 61, 47, 29, 53, 75],
    75: [29, 53, 47, 61, 13],
    61: [13, 53, 29],
    29: [13],
    53: [29, 13],
}
predecessors = {
    53: [47, 75, 61, 97],
    13: [97, 61, 29, 47, 75, 53],
    61: [97, 47, 75],
    47: [97, 75],
    29: [75, 97, 53, 61, 47],
    75: [97],
}


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 143
    assert part_A(f"day_{DAY}_input.txt") == 4957


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == 123
    assert part_B(f"day_{DAY}_input.txt") == 6938


def test_reorder_update() -> None:
    assert reorder_update([75, 97, 47, 61, 53], successors, predecessors) == [97, 75, 47, 61, 53]
    assert reorder_update([61, 13, 29], successors, predecessors) == [61, 29, 13]
    assert reorder_update([97, 13, 75, 29, 47], successors, predecessors) == [97, 75, 47, 29, 13]


def test_get_middle_element() -> None:
    assert get_middle_element([75, 47, 61, 53, 29]) == 61
    assert get_middle_element([97, 61, 53, 29, 13]) == 53
    assert get_middle_element([75, 29, 13]) == 29


def test_is_sorted() -> None:
    assert is_sorted([75, 47, 61, 53, 29], successors, predecessors)
    assert is_sorted([97, 61, 53, 29, 13], successors, predecessors)
    assert is_sorted([75, 29, 13], successors, predecessors)
    assert not is_sorted([75, 97, 47, 61, 53], successors, predecessors)
    assert not is_sorted([61, 13, 29], successors, predecessors)
    assert not is_sorted([97, 13, 75, 29, 47], successors, predecessors)
