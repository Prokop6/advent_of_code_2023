from advent_of_code_2023.src.day_2 import utils

import pytest


@pytest.mark.parametrize("sample,expected", [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 1"),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 2"),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 3"),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 4"),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", "Game 5")
])
def test_spliting_record(sample, expected):
  assert (expected == utils.get_segments(sample)[0])


@pytest.mark.parametrize("sample,expected", [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 2),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 3),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 4),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 5)
])
def test_getting_game_number(sample, expected):

  game_data, _ = utils.get_segments(sample)

  assert (expected == utils.get_game_no(game_data))


@pytest.mark.parametrize("sample,expected", [
    ("3 blue, 4 red", (4, 0, 3)),
    ("1 blue, 2 green", (0, 2, 1)),
    ("8 green, 6 blue, 20 red", (20, 8, 6)),
    ("5 blue, 4 red, 13 green", (4, 13, 5)),
])
def test_getting_rgb_data(sample, expected):
  assert (expected == utils.get_rgb_values(sample))


@pytest.mark.parametrize("sample,expected", [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (4, 2, 6)),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (1, 3, 4)),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", (20, 13, 6)),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", (14, 3, 15)),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (6, 3, 2))
])
def test_get_minimal_set(sample, expected):
  new_game = utils.parse_record(sample)

  assert (expected == new_game.get_minimal_set())
