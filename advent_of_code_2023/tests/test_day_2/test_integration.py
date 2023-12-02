from advent_of_code_2023.src.day_2 import part_1, part_2

import os


def get_data(file):
  data: str

  with open(os.path.join(os.getcwd(), "inputs", file), "r") as file:
    data = file.read()

  return data


def test_part_1_solution():

  assert (part_1.app(get_data("sample_2a.txt")) == 8)


def test_part_2_solution():

  assert (part_2.app(get_data("sample_2a.txt")) == 2286)
