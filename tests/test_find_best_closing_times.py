from stripe_interview.find_best_closing_times import find_best_closing_times

def test_find_best_closing_times():
  assert find_best_closing_times("BEGIN Y Y END \nBEGIN N N END") == [2, 0]
  assert find_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END") == [2]
