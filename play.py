#!/usr/bin/env python3

import ast
from collections import defaultdict
import random

NUMBER_MIN = 1
NUMBER_MAX = 20
LIST_SIZE_MIN = 3
LIST_SIZE_MAX = 6
TARGET_MIN = 10
TARGET_MAX = 100
OPS = ['Add', 'Sub', 'Mult', 'Div']

# TODO: guarantee the expression contains the ops in a list. generate this list with a 50% chance for each op in OPS
def random_expression(leaves):
  if len(leaves) == 1: return ast.Constant(value=leaves[0])
  split = random.randint(1, len(leaves)-1)
  left = random_expression(leaves[:split])
  right = random_expression(leaves[split:])
  op = getattr(ast, random.choice(OPS))
  return ast.BinOp(left=left, op=op(), right=right)

class Visitor(ast.NodeVisitor):
  def __init__(self, counts):
    self.counts = counts
    self.used = defaultdict(int)
    self.error = ""

  def visit_BinOp(self, node):
    op = type(node.op).__name__
    if op not in OPS: self.error = f"Can only use ops from {OPS}, got {op}"; return
    self.generic_visit(node)

  def visit_Constant(self, node):
    if node.value not in self.counts.keys(): self.error = f"Can only use numbers from the list, got '{node.value}'"; return
    if self.used[node.value] + 1 > self.counts[node.value]: self.error = 'Can only use each number in the list once'; return
    self.used[node.value] += 1
    self.generic_visit(node)

if __name__ == '__main__':
  while True:
    numbers = []
    counts = defaultdict(int)
    for i in range(random.randint(LIST_SIZE_MIN, LIST_SIZE_MAX)):
      num = random.randint(NUMBER_MIN, NUMBER_MAX)
      numbers.append(num)
      counts[num] += 1
    target_expr = ast.unparse(random_expression(numbers))
    try: target = eval(compile(target_expr, '<string>', 'eval'))
    except ZeroDivisionError: continue # TODO: add 'Pow' to OPS and catch OverflowError without stalling
    if target.is_integer() and TARGET_MIN <= target <= TARGET_MAX: break
  print(numbers)
  print(f'Target: {int(target)}') # explicit cast to int to remove the trailing .0

  while True:
    input_expr = input('Expression: ')
    if input_expr == 'I GIVE UP': print(target_expr); break
    nv = Visitor(counts)
    nv.visit(ast.parse(input_expr))
    if nv.error: print(nv.error); continue
    if nv.used != counts: print(f'Must use every value in the list {numbers}, got {list(nv.used)}'); continue # FIXME: list(nv.used) omits multiplicity
    try: result = eval(compile(input_expr, '<string>', 'eval'))
    except Exception as e: print(e); continue
    if result == target: print("Correct!"); break
    print(f'Incorrect (got {result}, expected {target})')
