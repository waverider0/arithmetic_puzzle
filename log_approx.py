#!/usr/bin/env python3

# log10(2) = 0.3
# log10(5) = 0.7
# 1 / log10(2) = 3.3
# 1 / log10(e) = 2.3

from math import log, log2, log10
import random

if __name__ == '__main__':
  f = random.choice(['pow', 'log10', 'log2', 'ln'])

  if f == 'pow':
    a,x = random.randint(2, 20), random.randint(1, 20)
    exact = a ** x
    ans = float(input(f'{a} ** {x} = '))
  else:
    x = random.randint(2,500)
    exact = (log if f=='ln' else log10 if f=='log10' else log2)(x)
    ans = float(input(f"{f}({x}) = "))

  print(f'Exact: {round(exact, 2)}')
  print(f'Error: {round((ans - exact) / exact * 100, 2)}%')
