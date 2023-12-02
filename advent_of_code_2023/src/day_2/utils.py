import re

class Sample():
  __red: int
  __green: int
  __blue: int

  def __init__(self, red=0, green=0, blue=0):
    self.__blue = blue
    self.__red = red
    self.__green = green

  def get_red(self):
    return self.__red

  def get_blue(self):
    return self.__blue

  def get_green(self):
    return self.__green


class Game():

  __number: int
  __samples: 'list[Sample]'

  def __init__(self, game_number: int):
    self.__number = game_number
    self.__samples = []

  def add_sample(self, r: int, g: int, b: int):
    sample = Sample(r, g, b)

    self.__samples.append(sample)

  def get_game_number(self):
    return self.__number

  def get_max_red(self):

    max_red: int = 0

    for sample in self.__samples:
      if sample.get_red() > max_red:
        max_red = sample.get_red()

    return max_red

  def get_max_green(self):

    max_green: int = 0

    for sample in self.__samples:
      if sample.get_green() > max_green:
        max_green = sample.get_green()

    return max_green

  def get_max_blue(self):

    max_blue: int = 0

    for sample in self.__samples:
      if sample.get_blue() > max_blue:
        max_blue = sample.get_blue()

    return max_blue

  def get_id_if_possible(self,
                         max_red: int,
                         max_green: int,
                         max_blue: int) -> int:

    if self.get_max_red() > max_red:
      return 0

    if self.get_max_green() > max_green:
      return 0

    if self.get_max_blue() > max_blue:
      return 0

    return self.get_game_number()

  def get_minimal_set(self):
    return (
        self.get_max_red(),
        self.get_max_green(),
        self.get_max_blue()
    )


def get_game_no(data: str) -> int:

  PATTERN = r'\s*game\s*(?P<game_no>\d{1,2})'

  re_pattern: re.Pattern = re.compile(PATTERN, re.IGNORECASE)

  matches: re.Match = re_pattern.match(data)  # type: ignore

  if matches == None:
    raise ValueError(data)

  return int(matches.group("game_no"))


def get_rgb_values(data: str) -> 'tuple[int,int,int]':

  PATTERN: str = r'\s*(?:(?:(?P<blue>\d{1,2})\s*blue|(?P<red>\d{1,2})\s*red|\s*(?P<green>\d{1,2})\s*green),*\s*){1,3}'

  re_pattern: re.Pattern = re.compile(PATTERN, re.IGNORECASE)

  matches: re.Match = re_pattern.match(data)  # type: ignore

  if matches == None:
    raise ValueError(data)

  r: int = 0
  g: int = 0
  b: int = 0

  if matches.group("red"):
    r = int(matches.group("red"))

  if matches.group("green"):
    g = int(matches.group("green"))

  if matches.group("blue"):
    b = int(matches.group("blue"))

  return (r, g, b)


def get_rows(data: str) -> 'list[str]':

  return data.strip().split("\n")


def get_segments(data: str) -> 'tuple[str, list[str]]':

  separated: list[str] = data.split(":")

  match = separated[0]

  results: list[str] = separated[1].split(";")

  return (match, results)


def parse_record(data: str) -> Game:

  game_number_data, matches_data = get_segments(data)

  game_number = get_game_no(game_number_data)

  new_game = Game(game_number)

  for match in matches_data:
    match_results = get_rgb_values(match)

    new_game.add_sample(match_results[0],
                        match_results[1],
                        match_results[2])

  return new_game
