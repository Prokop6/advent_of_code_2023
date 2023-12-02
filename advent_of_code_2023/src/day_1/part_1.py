import os
from advent_of_code_2023.src.day_1 import utils


def app(filename: str) -> int:

  data: str 

  with open(os.path.join(os.getcwd(), 'inputs', filename), "r") as file:
    data = file.read()

    clear_data = data.strip()

    values = [value for value in clear_data.split("\n")]

    clear_values: list[int] = []

    for value in values:
      first_digit:int = int(utils.get_first_digit(value))

      last_digit:int = int(utils.get_last_digit(value))

      clear_values.append(first_digit*10+last_digit)
      
  result = sum(clear_values)

  return result
