from day_03 import part_A, part_B, read_file, convert, Number, Symbol, get_numbers_near_symbol


def test_number() -> None:
    assert Number(123, 0, 0).x_max == 2


def test_read_file() -> None:
    data = read_file("day_03_input_sample.txt")
    assert data[0][0] == "4"
    assert data[0][1] == "6"


def test_convert() -> None:
    data = read_file("day_03_input_sample.txt")
    numbers, symbols = convert(data)
    assert numbers[0].value == 467
    assert numbers[0].x == 0
    assert numbers[0].y == 0
    assert len(numbers) == 10
    assert symbols[0].value == "*"
    assert symbols[0].x == 3
    assert symbols[0].y == 1
    assert len(symbols) == 6


def test_get_numbers_near_symbol() -> None:
    numbers = [Number(123, 10, 10)]
    symbols = [Symbol("#", 9, 10)]
    assert get_numbers_near_symbol(numbers, symbols) == [123]
    symbols = [Symbol("#", 13, 10)]
    assert get_numbers_near_symbol(numbers, symbols) == [123]
    symbols = [Symbol("#", 9, 9)]
    assert get_numbers_near_symbol(numbers, symbols) == [123]
    symbols = [Symbol("#", 13, 9)]
    assert get_numbers_near_symbol(numbers, symbols) == [123]
    symbols = [Symbol("#", 9, 11)]
    assert get_numbers_near_symbol(numbers, symbols) == [123]
    symbols = [Symbol("#", 13, 9)]
    assert get_numbers_near_symbol(numbers, symbols) == [123]
    symbols = [Symbol("#", 8, 9)]
    assert get_numbers_near_symbol(numbers, symbols) == []
    symbols = [Symbol("#", 14, 9)]
    assert get_numbers_near_symbol(numbers, symbols) == []
    symbols = [Symbol("#", 9, 8)]
    assert get_numbers_near_symbol(numbers, symbols) == []
    symbols = [Symbol("#", 9, 12)]
    assert get_numbers_near_symbol(numbers, symbols) == []
    symbols = [Symbol("#", 10, 12)]
    assert get_numbers_near_symbol(numbers, symbols) == []


def test_part_A():
    assert part_A("day_03_input_sample.txt") == 4361


def test_part_B():
    assert part_B("day_03_input_sample.txt") == 467835
