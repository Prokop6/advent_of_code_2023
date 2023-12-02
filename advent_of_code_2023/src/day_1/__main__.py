import os
import sys

sys.path.append(os.getcwd())

from advent_of_code_2023.src.day_1 import part_1
from advent_of_code_2023.src.day_1 import part_2

if __name__ == "__main__":
  print("Result of part 1:")
  print(part_1.app("1.txt"))

  print("Result of part 2:")
  print(part_2.app("1.txt"))
