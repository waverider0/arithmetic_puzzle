#!/usr/bin/env python3

import random
import readline
import threading
import time

OPS = ['+', '-', '*', '/']
ADD_L = [2, 100]
ADD_R = [2, 100]
MUL_L = [2, 12]
MUL_R = [2, 100]
DURATION_SECONDS = 120

if __name__ == '__main__':
  score = 0
  running = threading.Event()
  running.set()
  threading.Timer(DURATION_SECONDS, running.clear).start()

  while running.is_set():
    op = random.choice(OPS)
    match op:
      case '+' | '-':
        a = random.randint(*ADD_L)
        b = random.randint(*ADD_R)
        exact = a+b if op == '+' else a-b
        ans = None
        while ans != exact: ans = int(input(f'{a} {op} {b} = ')) # FIXME: a non-number typo breaks the program and ends the game prematurely
        score += 1
        print(f'Score: {score}')
      case '*':
        a = random.randint(*MUL_L)
        b = random.randint(*MUL_R)
        exact = a * b
        ans = None
        while ans != exact: ans = int(input(f'{a} * {b} = '))
        score += 1
        print(f'Score: {score}')
      case '/':
        a = random.randint(*MUL_L)
        b = random.randint(*MUL_R)
        exact = a / b
        ans = None
        while ans is None or abs((ans - exact) / exact > 0.01): ans = float(input(f'{a} / {b} = '))
        score += 1
        print(f'Score: {score}')
