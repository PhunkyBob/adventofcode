from day_01 import part_A, part_B, replace_digits, get_first_and_last, keep_only_digits


def test_part_A() -> None:
    assert part_A("day_01_input_sample.txt") == 142


def test_apply_transformation() -> None:
    assert replace_digits("two1nine") == "two2two1nine9nine"
    assert replace_digits("eightwothree") == "eight8eightwo2twothree3three"


def test_part_B() -> None:
    assert part_B("day_01_input_sample2.txt") == 281


def test_replace_digits() -> None:
    assert replace_digits("one1two") == "one1one1two2two"
    assert replace_digits("three3four") == "three3three3four4four"
    assert replace_digits("five5six") == "five5five5six6six"
    assert replace_digits("seven7eight") == "seven7seven7eight8eight"
    assert replace_digits("nine9zero") == "nine9nine9zero"


def test_replace_digits_edge_cases() -> None:
    assert replace_digits("") == ""  # Empty string
    assert replace_digits("1234567890") == "1234567890"  # All digits
    assert replace_digits("abcdefg") == "abcdefg"  # No digits


def test_keep_only_digits() -> None:
    assert keep_only_digits("one1two2three3") == "123"
    assert keep_only_digits("four4five5six6") == "456"
    assert keep_only_digits("seven7eight8nine9") == "789"
    assert keep_only_digits("zero0one1two2") == "012"


def test_keep_only_digits_edge_cases() -> None:
    assert keep_only_digits("") == ""  # Empty string
    assert keep_only_digits("1234567890") == "1234567890"  # All digits
    assert keep_only_digits("abcdefg") == ""  # No digits
    assert keep_only_digits(" 1 2 3 ") == "123"  # Digits with spaces
    assert keep_only_digits("1" * 1000) == "1" * 1000  # Long string of the same digit


def test_get_first_and_last() -> None:
    assert get_first_and_last("hello") == "ho"
    assert get_first_and_last("a") == "aa"
    assert get_first_and_last("abc") == "ac"
    assert get_first_and_last("1234567890") == "10"


def test_get_first_and_last_edge_cases() -> None:
    assert get_first_and_last("") == ""  # Empty string
    assert get_first_and_last(" ") == "  "  # Single space
    assert get_first_and_last("  ") == "  "  # Two spaces
    assert get_first_and_last("a" * 1000) == "aa"  # Long string of the same character
