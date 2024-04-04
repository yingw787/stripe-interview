#!/usr/bin/env python3

import pytest

from stripe_interview.find_best_closing_time import find_best_closing_time

def test_find_best_closing_time():
  assert find_best_closing_time("Y Y N N") == 2

def test_2_find_best_closing_time():
    print("test_find_best_closing_time")
    assert find_best_closing_time("Y Y Y N N N N" ) == 3
    assert find_best_closing_time("") == 0

    assert find_best_closing_time("Y") == 1


    assert find_best_closing_time("N N N N" ) == 0
    assert find_best_closing_time("Y Y Y Y" ) == 4
    assert find_best_closing_time("N Y Y Y Y N N N Y N N Y Y N N N N Y Y N N Y N N N" ) == 5
    assert find_best_closing_time("N N N N N Y Y Y N N N N Y Y Y N N N Y N Y Y N Y N" ) == 0
    assert find_best_closing_time("Y Y N N N Y Y N Y Y N N N Y Y N N Y Y Y N Y N Y Y" ) == 25
