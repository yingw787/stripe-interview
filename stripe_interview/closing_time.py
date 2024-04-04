#!/usr/bin/env python3


def compute_penalty(store_log: str, closing_time: int) -> int:
  # Parse store log into a Python list
  storelog_as_list = store_log.split(' ')

  # From the closing time, create a Python list with length equivalent to the
  # length of the parsed store log, with definitions on when the store is open
  # and closed
  #
  # Create 1s where store is open, and 0s when store is closed
  store_open_hours = [1] * closing_time
  remaining_closed_hours = [0] * (len(storelog_as_list) - len(store_open_hours))
  store_open_hours += remaining_closed_hours

  # Zip the two lists together - cannot use dict because dict has unique keys
  combined_storelog = list(zip(storelog_as_list, store_open_hours))

  penalty = 0

  for item in list(combined_storelog):
    has_customer = item[0] == 'Y'
    is_store_open = item[1] == 1

    if (
      (has_customer and not is_store_open) or
      (not has_customer and is_store_open)
    ):
      penalty += 1

  # Return the count of the final items.
  return penalty
