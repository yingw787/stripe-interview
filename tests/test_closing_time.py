#!/usr/bin/env python3

import pytest

from stripe_interview.closing_time import compute_penalty

def test_compute_penalty_success():
  assert compute_penalty("Y Y N Y", 0) == 3
  assert compute_penalty("N Y N Y", 2) == 2
  assert compute_penalty("Y Y N Y", 4) == 1
