from day_17 import part_A, part_B, DAY, Computer


def test_1() -> None:
    cpu = Computer()
    cpu.register_c = 9
    cpu.program = [2, 6]
    cpu.run()
    assert cpu.register_b == 1


def test_2() -> None:
    cpu = Computer()
    cpu.register_a = 10
    cpu.program = [5, 0, 5, 1, 5, 4]
    result = cpu.run()
    assert result == [0, 1, 2]


def test_3() -> None:
    cpu = Computer()
    cpu.register_a = 2024
    cpu.program = [0, 1, 5, 4, 3, 0]
    result = cpu.run()
    assert result == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert cpu.register_a == 0


def test_4() -> None:
    cpu = Computer()
    cpu.register_b = 29
    cpu.program = [1, 7]
    cpu.run()
    assert cpu.register_b == 26


def test_5() -> None:
    cpu = Computer()
    cpu.register_b = 2024
    cpu.register_c = 43690
    cpu.program = [4, 0]
    cpu.run()
    assert cpu.register_b == 44354


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == "4,6,3,5,6,3,5,2,1,0"
    assert part_A(f"day_{DAY}_input.txt") == "2,0,7,3,0,3,1,3,7"


def test_6() -> None:
    cpu = Computer()
    cpu.register_a = 117440
    cpu.program = [0, 3, 5, 4, 3, 0]
    result = cpu.run()
    assert result == cpu.program


def test_part_B() -> None:
    assert part_B(f"day_{DAY}_input_sample2.txt") == 117440
    # assert part_B(f"day_{DAY}_input_sample2.txt") == 64
    # assert part_B(f"day_{DAY}_input.txt") == 458
