#!/usr/bin/env python3

def fibanocci(n: int) -> int:
  if n < 2:
    return n

  return fibanocci(n - 1) + fibanocci(n - 2)

if __name__=="__main__":
  print(fibanocci(10))
