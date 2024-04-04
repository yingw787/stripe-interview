#!/usr/bin/env python3

import pytest

from stripe_interview.closing_time import compute_penalty

def test_compute_penalty_success():
  assert compute_penalty("Y Y N Y", 0) == 3
  assert compute_penalty("N Y N Y", 2) == 2
  assert compute_penalty("Y Y N Y", 4) == 1

  assert compute_penalty("", 0) == 0

  assert compute_penalty("Y Y N", 0) == 2


def test_compute_penalty():
    print("test_compute_penalty")
    assert compute_penalty("Y Y N Y" , 1) == 2
    assert compute_penalty("Y Y Y N N N N" , 0) == 3
    assert compute_penalty("Y Y Y N N N N" , 7) == 4
    assert compute_penalty("Y Y Y N N N N" , 3) == 0
    assert compute_penalty("", 0) == 0
    assert compute_penalty("Y N Y N N N N" , 3) == 1
