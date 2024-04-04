#!/usr/bin/env python3

from stripe_interview.closing_time import compute_penalty

def find_best_closing_time(store_log: str) -> int:
  # Start with the highest penalty, which upper bound is the length of the store
  # log
  lowest_penalty = len(store_log)
  best_closing_time = 0

  # Compute the penalty given a closing time from 0 to len(store_log) - 1. If
  # the penalty is lower, then replace lowest_penalty with the new penalty.
  for idx in range(len(store_log.split(' ')) + 1):
    new_penalty = compute_penalty(store_log, idx)
    if new_penalty < lowest_penalty:
      lowest_penalty = new_penalty
      best_closing_time = idx

  return best_closing_time
