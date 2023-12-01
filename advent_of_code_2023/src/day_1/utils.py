import re

def get_first_digit(sample: str) -> int:
  MASK = r'[a-z]*(\d)[\w]*'
  expression = re.compile(MASK, re.IGNORECASE)

  matches = expression.search(sample)

  if matches == None:
    raise ValueError()
  else: 
    return str(matches[1])

def get_last_digit(sample:str) -> int:
  
  MASK = r'[\w]*(\d)[a-z]*'
  expression = re.compile(MASK, re.IGNORECASE)

  matches = expression.search(sample)

  if matches == None:
    raise ValueError()
  else: 
    return matches[1]

def get_first_extended_digit(sample: str) -> int:
  
  MASK = r'(\d|one|two|three|four|five|six|seven|eight|nine){1}'
  expression = re.compile(MASK, re.IGNORECASE)

  matches = expression.search(sample)

  if matches == None:
    raise ValueError()

  
  return parse_verbose_digit(matches[1])

def get_last_extended_digit(sample: str) -> int:
  
  MASK = r'(\d|one|two|three|four|five|six|seven|eight|nine){1}'
  expression = re.compile(MASK, re.IGNORECASE)

  matches = expression.findall(sample)

  if matches == None:
    raise ValueError()

  
  return parse_verbose_digit(matches[-1])

def parse_verbose_digit(sample: str|int) -> int:
  
  verbose_digits = {
    '1': 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
  }

  return verbose_digits[sample.casefold()]