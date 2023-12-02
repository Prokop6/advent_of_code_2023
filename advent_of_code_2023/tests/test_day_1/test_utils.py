from advent_of_code_2023.src.day_1 import utils

import pytest

class TestGetFirstDigit():
  
  @pytest.mark.parametrize("sample,expected", [
    ("1", "1"),
    ("1abc", "1"),
    ("abc1", "1"),
    ("a1b2c", "1"),
  ])
  def test_get_first_digit(self, sample, expected):

    assert (expected == utils.get_first_digit(sample))

class TestGetLastDigit():
  
  @pytest.mark.parametrize("sample,expected", [
    ("1", "1"),
    ("1abc", "1"),
    ("abc1", "1"),
    ("a1b2c", "2"),
  ])
  def test_get_last_digit(self, sample, expected):

    assert (expected == utils.get_last_digit(sample))

class TestGetFirstExtendedDigit():

  @pytest.mark.parametrize("sample,expected", [
    ("two1nine",2),
    ("eightwothree",8),
    ("abcone2threexyz",1),
    ("xtwone3four",2),
    ("4nineeightseven2",4),
    ("zoneight234",1),
    ("7pqrstsixteen",7),
  ])
  def test_get_fist_extended_digit(self, sample, expected):
    assert (expected == utils.get_first_extended_digit(sample))

class TestGetLastExtendedDigit():

  @pytest.mark.parametrize("sample,expected", [
    ("two1nine",9),
    ("eightwothree",3),
    ("abcone2threexyz",3),
    ("xtwone3four",4),
    ("4nineeightseven2",2),
    ("zoneight234",4),
    ("7pqrstsixteen",6),
  ])
  def test_get_last_extended_digit(self, sample, expected):
    assert (expected == utils.get_last_extended_digit(sample))