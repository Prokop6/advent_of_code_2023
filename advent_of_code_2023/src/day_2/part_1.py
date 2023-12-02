from advent_of_code_2023.src.day_2 import utils

MAX_POSSIBLE_RED: int = 12
MAX_POSSIBLE_GREEN: int = 13
MAX_POSSIBLE_BLUE: int = 14

def app(data: str) -> int:
  result: int = 0

  rows: list[str] = utils.get_rows(data)
  games: list[utils.Game] = []

  for row in rows:

    new_game: utils.Game = utils.parse_record(row)

    games.append(new_game)

  for game in games:
    result += game.get_id_if_possible(
        MAX_POSSIBLE_RED,
        MAX_POSSIBLE_GREEN,
        MAX_POSSIBLE_BLUE
    )


  return result
