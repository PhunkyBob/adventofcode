from day_02 import Game, part_A, part_B


def test_game_class():
    game = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert game.id == 1
    assert game.blue == 6
    assert game.green == 2
    assert game.red == 4


def test_part_A():
    assert part_A("day_02_input_sample.txt") == 8


def test_part_B():
    assert part_B("day_02_input_sample.txt") == 2286
