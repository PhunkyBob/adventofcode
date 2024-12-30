from day_23 import part_A, part_B, DAY, get_three_connections, read_input


def test_count_three_connections() -> None:
    connections = read_input(f"day_{DAY}_input_sample.txt")
    assert len(get_three_connections(connections, "")) == 12
    assert len(get_three_connections(connections, "t")) == 7


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 7
    assert part_A(f"day_{DAY}_input.txt") == 1200


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample.txt") == "co,de,ka,ta"
    # assert part_A(f"day_{DAY}_input.txt") == "ag,gh,hh,iv,jx,nq,oc,qm,rb,sm,vm,wu,zr"
