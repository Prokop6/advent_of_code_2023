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

  def add_sample(r: int, g: int, b: int):
    sample = Sample(r, g, b)

    self.__samples.append(sample)

  def get_game_number(self):
    return self.__number

  def get_max_red(self):

    max_red: int = 0

    for sample in self.__samples:
      if sample.get_max_red() > max_red:
        max_red = sample.get_max_red()

    return max_red

  def get_max_green(self):

    max_green: int = 0

    for sample in self.__samples:
      if sample.get_max_green() > max_green:
        max_green = sample.get_max_green()

    return max_green

  def get_max_blue(self):

    max_blue: int = 0

    for sample in self.__samples:
      if sample.get_max_blue() > max_blue:
        max_blue = sample.get_max_blue()

    return max_blue


def get_game_no(data: str) -> int:

  PATTERN = r'game\s*(?P<game_no>\d{1,2}):'

  re_patter = re.compile(PATTERN, re.IGNORECASE)

  matches = re_pattern.search(data)

  return matches["game_no"]


def get_rgb_values(data: str) -> 'tuple[int]':

  PATTERN: str = r'\s*(?:(?:(?P<blue>\d{1,2})\s*blue|(?P<red>\d{1,2})\s*red|\s*(?P<green>\d{1,2})\s*green),*\s*){1,3}'

  re_pattern: re.Pattern = re.complie(PATTERN, re.IGNORECASE)

  matches: re.Matches = re_pattern.search(data)

  r: int = 0
  g: int = 0
  b: int = 0

  if matches["red"]:
    r = matches["red"]

  if matches["green"]:
    g = matches["green"]

  if matches["blue"]:
    b = matches["blue"]

  return (r, g, b)
