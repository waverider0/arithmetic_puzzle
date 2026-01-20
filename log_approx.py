#!/usr/bin/env python3

# log10(2) = 0.3
# log10(5) = 0.7
# 1 / log10(e) = 2.3

import math
import random

if __name__ == '__main__':
  problem_type = random.choice(['pow', 'log10', 'ln'])

  if problem_type == 'pow':
    a = random.randint(2, 20)
    x = random.randint(1, 20)
    exact = a ** x
    ans = float(input(f'{a} ** {x} = '))
  elif problem_type == 'log10':
    x = random.randint(2, 500)
    exact = math.log10(x)
    ans = float(input(f'log10({x}) = '))
  else:
    x = random.randint(2, 500)
    exact = math.log(x)
    ans = float(input(f'ln({x}) = '))

  print(f'Exact: {round(exact, 2)}')
  print(f'Error: {round((ans - exact) / exact * 100, 2)}%')
