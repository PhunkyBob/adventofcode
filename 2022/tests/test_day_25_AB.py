import pytest
import sys

sys.path.append("..")
from day_25_AB import snafu_to_int, int_to_snafu

DAY = "25"

INPUT_SAMPLE = f"day_{DAY}_input_sample.txt"
INPUT = f"day_{DAY}_input.txt"


def test_snafu_to_int():
    assert snafu_to_int("1=-0-2") == 1747
    assert snafu_to_int("12111") == 906
    assert snafu_to_int("2=0=") == 198
    assert snafu_to_int("21") == 11
    assert snafu_to_int("2=01") == 201
    assert snafu_to_int("111") == 31
    assert snafu_to_int("20012") == 1257
    assert snafu_to_int("112") == 32
    assert snafu_to_int("1=-1=") == 353
    assert snafu_to_int("1-12") == 107
    assert snafu_to_int("12") == 7
    assert snafu_to_int("1=") == 3
    assert snafu_to_int("122") == 37


def test_int_to_snafu():
    assert int_to_snafu(1) == "1"
    assert int_to_snafu(2) == "2"
    assert int_to_snafu(3) == "1="
    assert int_to_snafu(4) == "1-"
    assert int_to_snafu(5) == "10"
    assert int_to_snafu(6) == "11"
    assert int_to_snafu(7) == "12"
    assert int_to_snafu(8) == "2="
    assert int_to_snafu(9) == "2-"
    assert int_to_snafu(10) == "20"
    assert int_to_snafu(15) == "1=0"
    assert int_to_snafu(20) == "1-0"
    assert int_to_snafu(2022) == "1=11-2"
    assert int_to_snafu(12345) == "1-0---0"
    assert int_to_snafu(314159265) == "1121-1110-1=0"


if __name__ == "__main__":
    pass
