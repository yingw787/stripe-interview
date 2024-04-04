#!/usr/bin/env python3

import pytest

from stripe_interview.fibanocci import fibanocci

def test_fibanocci():
  assert fibanocci(0) == 0
  assert fibanocci(1) == 1

def test_fibanocci_common_cases():
    assert fibanocci(5) == 5
    assert fibanocci(10) == 55
    assert fibanocci(12) == 144

def test_fibanocci_negative_input():
    # Assuming your function raises a ValueError for negative inputs
    with pytest.raises(ValueError):
        fibanocci(-1)
