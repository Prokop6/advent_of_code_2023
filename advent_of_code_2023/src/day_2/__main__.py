import os
import sys

sys.path.append(os.getcwd())

from advent_of_code_2023.src.day_2 import part_1
from advent_of_code_2023.src.day_2 import part_2

if __name__ == "__main__":
  data: str
  with open(os.path.join(os.getcwd(), "inputs", "2.txt"), "r") as file:
    data = file.read()
  
  print("Result for part 1:")
  print(part_1.app(data))
  print("Result for part 2:")
  print(part_2.app(data))
