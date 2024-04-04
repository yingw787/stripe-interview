
from stripe_interview.find_best_closing_time import find_best_closing_time

def find_best_closing_times(aggregate_log):
  best_closing_times = []

  begin_idx = None
  end_idx = None

  import ipdb
  ipdb.set_trace()

  for i in range(len(aggregate_log)):
    for j in range(i, len(aggregate_log)):
      possible_begin = aggregate_log[i:]

      if possible_begin.startswith("BEGIN"):
        begin_idx = i

      possible_end = aggregate_log[j:]

      if possible_end.startswith("END"):
        end_idx = j

      if begin_idx != None and end_idx != None:
        proper_log = aggregate_log[i+len("BEGIN"):j]
        proper_log = proper_log.strip()
        proper_log = proper_log.replace("\n", "")

        best_closing_time = find_best_closing_time(proper_log)

        best_closing_times += [best_closing_time]

        begin_idx = None
        end_idx = None



  return best_closing_times
