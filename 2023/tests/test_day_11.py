from day_11 import DAY, part_A, part_B, expand_universe, read_input, Coordinate, get_manhattan_distance
from itertools import combinations_with_replacement


def test_expand_universe():
    universe = read_input(f"day_{DAY}_input_sample.txt")
    expanded_universe = expand_universe(universe)
    expected_universe = read_input(f"day_{DAY}_input_sample_extended.txt")
    assert expanded_universe == expected_universe


def test_expand_universe_2():
    universe = read_input(f"day_{DAY}_input_sample.txt")
    expanded_universe = expand_universe(universe, 10)
    total = sum(
        get_manhattan_distance(coord1, coord2)
        for coord1, coord2 in combinations_with_replacement(expanded_universe, 2)
    )
    assert total == 1030
    expanded_universe = expand_universe(universe, 100)
    total = sum(
        get_manhattan_distance(coord1, coord2)
        for coord1, coord2 in combinations_with_replacement(expanded_universe, 2)
    )
    assert total == 8410


def test_part_A():
    assert part_A(f"day_{DAY}_input_sample.txt") == 374


def test_part_B():
    assert part_B(f"day_{DAY}_input_sample.txt") == 82000210
