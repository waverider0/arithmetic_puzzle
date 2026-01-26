#!/usr/bin/env python3

import random
import threading
import time

OPS = ['Add', 'Sub', 'Mul', 'Div']
ADD_MIN = (2,1000)
ADD_MAX = (2,1000)
MUL_MIN = (2,100)
MUL_MAX = (2,100)
DURATION_SECONDS = 120

if __name__ == '__main__':
  score = 0
  running = threading.Event()
  timer = threading.Timer(DURATION_SECONDS, running.clear)

  running.set()
  timer.start()

  while running.is_set():
    op = random.choice(OPS)
    if op in ['Add', 'Sub']: pass
    elif op in ['Mul', 'Div']: pass

  print(score)
