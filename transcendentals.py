#!/usr/bin/env python3

# log10(2) = 0.3
# log10(3) = 0.48
# log10(5) = 0.7
# 1 / log10(e) = 2.3

import math
import random
import readline

#
# exponentials
#

def make_pow():
  a = random.randint(2, 20)
  x = random.randint(2, 10)
  return f'{a}^{x} = ', a ** x

def make_exp():
  x = random.uniform(0.5, 5.0)
  return f'e^{x:.2f} = ', math.exp(x)

def make_ln():
  x = random.randint(2, 1000)
  return f'ln({x}) = ', math.log(x)

def make_log2():
  x = random.randint(2, 1000)
  return f'log2({x}) = ', math.log2(x)

def make_log10():
  x = random.randint(2, 1000)
  return f'log10({x}) = ', math.log10(x)

#
# trig
#

def make_sin():
  x_deg = random.randint(-360, 360)
  return f'sin({x_deg}°) = ', math.sin(math.radians(x_deg))

def make_cos():
  x_deg = random.randint(-360, 360)
  return f'cos({x_deg}°) = ', math.cos(math.radians(x_deg))

def make_tan():
  x_deg = random.randint(-89, 89)
  return f'tan({x_deg}°) = ', math.tan(math.radians(x_deg))

def make_asin():
  x = round(random.uniform(-0.99, 0.99), 2)
  return f'asin({x}) = ', math.degrees(math.asin(x))

def make_acos():
  x = round(random.uniform(-0.99, 0.99), 2)
  return f'acos({x}) = ', math.degrees(math.acos(x))

def make_atan():
  x = round(random.uniform(-10, 10), 2)
  return f'atan({x}) = ', math.degrees(math.atan(x))

#
# hyperbolic trig
#

def make_sinh():
  x = round(random.uniform(-5, 5), 2)
  return f'sinh({x}) = ', math.sinh(x)

def make_cosh():
  x = round(random.uniform(-5, 5), 2)
  return f'cosh({x}) = ', math.cosh(x)

def make_tanh():
  x = round(random.uniform(-5, 5), 2)
  return f'tanh({x}) = ', math.tanh(x)

def make_asinh():
  x = round(random.uniform(-10, 10), 2)
  return f'asinh({x}) = ', math.asinh(x)

def make_acosh():
  x = round(random.uniform(1, 10), 2)
  return f'acosh({x}) = ', math.acosh(x)

def make_atanh():
  x = round(random.uniform(-0.99, 0.99), 2)
  return f'atanh({x}) = ', math.atanh(x)

functions = {
  'pow'   : make_pow,
  'exp'   : make_exp,
  'ln'    : make_ln,
  'log2'  : make_log2,
  'log10' : make_log10,

  'sin'   : make_sin,
  'cos'   : make_cos,
  'tan'   : make_tan,
  'asin'  : make_asin,
  'acos'  : make_acos,
  'atan'  : make_atan,

  'sinh'  : make_sinh,
  'cosh'  : make_cosh,
  'tanh'  : make_tanh,
  'asinh' : make_asinh,
  'acosh' : make_acosh,
  'atanh' : make_atanh,
}

if __name__ == '__main__':
  name = random.choice(list(functions.keys()))
  prompt, exact = functions[name]()
  ans = float(input(prompt))
  print(f'Exact: {round(exact, 2)} ({round((ans - exact) / exact * 100, 2)}% error)')
