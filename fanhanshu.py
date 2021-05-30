import numpy as np
from scipy.optimize import root


def func(x):
    y = x +1
    return y


sol = root(func - 1, 3)
print(sol.x, sol.fun)