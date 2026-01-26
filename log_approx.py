#!/usr/bin/env python3

# log10(2) = 0.3
# log10(3) = 0.48
# log10(5) = 0.7
# 1 / log10(e) = 2.3

from math import log, log2, log10
import random
import readline

if __name__ == '__main__':
  fn = random.choice(['pow', 'log10', 'log2', 'ln'])

  if fn == 'pow':
    a = random.randint(2, 20)
    x = random.randint(2, 20)
    exact = a ** x
    ans = float(input(f'{a}^{x} = '))
  else:
    x = random.randint(2, 1000)
    exact = (log if fn=='ln' else log2 if fn=='log2' else log10)(x)
    ans = float(input(f'{fn}({x}) = '))

  print(f'Exact: {round(exact, 2)} ({round((ans - exact) / exact * 100, 2)}% error)')
