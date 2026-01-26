#!/usr/bin/env python3

import random
import threading
import time

OPS = ['Add', 'Sub', 'Mul', 'Div']
ADD_L = [2, 1000]
ADD_R = [2, 1000]
MUL_L = [2, 100]
MUL_R = [2, 100]
DURATION_SECONDS = 120

if __name__ == '__main__':
  score = 0
  running = threading.Event()
  timer = threading.Timer(DURATION_SECONDS, running.clear)

  running.set()
  timer.start()

  while running.is_set():
    op = random.choice(OPS)
    match op:
      case 'Add':
        a = random.randint(*ADD_L)
        b = random.randint(*ADD_R)
        correct = a + b
        answer = int(input(f'{a} + {b} = '))
      case 'Sub':
        a = random.randint(*ADD_L)
        b = random.randint(*ADD_R)
        correct = a - b
        answer = int(input(f'{a} - {b} = '))
      case 'Mul':
        pass
      case 'Div':
        pass

  print(score)
