
from advent_of_code_2023.src.day_2 import utils

def app(data: str) -> int:
  result: int = 0

  rows: list[str] = utils.get_rows(data)
  games: list[utils.Game] = []

  for row in rows:

    new_game: utils.Game = utils.parse_record(row)

    games.append(new_game)

  for game in games:
    red_dice, green_dice, blue_dice = game.get_minimal_set()

    power: int = red_dice * green_dice * blue_dice

    result += power


  return result

