"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a:float, b:float) -> float:
    return a*b

def id(a:float) -> float:
    return a

def add(a:float, b:float) -> float:
    return a + b

def neg(a:float) -> float:
    return -1 * a

def lt(a:float, b:float) -> bool:
    return a < b

def eq(a:float, b:float) -> bool:
    return a == b

def is_close(a:float, b:float, eps:float=0.01) -> bool:
    return abs(a-b) <= eps

def sigmoid(x:float) -> float:
    if x>= 0: 
        return 1/(1 + math.exp(-x))
    return x/(1 + math.exp(x))

def relu(x:float) -> float:
    return max(0, x)

def log(x:float) -> float:
    return math.log2(x)

def exp(x:float) -> float:
    return math.exp(x)

def inv(x:float) -> float:
    return 1/x

def log_back(x:float, y:float) -> float:
    return y * (1/x)

def inv_back(x:float, y:float) -> float:
    return y * (-1/(x)**2)

def relu_back(x:float, y:float) -> float:
    return 0 if x ==0 else y*x

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
