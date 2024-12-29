from day_22 import part_A, DAY, mix, prune, evolve_secret


def test_mix() -> None:
    assert mix(42, 15) == 37


def test_prune() -> None:
    assert prune(100000000) == 16113920


def test_evolve_secret() -> None:
    secret = 123
    generator = evolve_secret(secret)
    assert next(generator) == 15887950
    assert next(generator) == 16495136
    assert next(generator) == 527345
    assert next(generator) == 704524
    assert next(generator) == 1553684
    assert next(generator) == 12683156
    assert next(generator) == 11100544
    assert next(generator) == 12249484
    assert next(generator) == 7753432
    assert next(generator) == 5908254


def test_part_A() -> None:
    assert part_A(f"day_{DAY}_input_sample.txt") == 37327623
    assert part_A(f"day_{DAY}_input.txt") == 0
