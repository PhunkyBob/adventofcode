from day_23 import part_A, DAY, count_three_connections, read_input


def test_count_three_connections() -> None:
    connections = read_input(f"day_{DAY}_input_sample.txt")
    assert count_three_connections(connections, "") == 12
    assert count_three_connections(connections, "t") == 7


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 2024
    assert part_A(f"day_{DAY}_input.txt") == 45213383376616
