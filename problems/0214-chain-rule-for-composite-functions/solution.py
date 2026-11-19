import numpy as np
import math

def func(rule,x):
    if rule=='sin':
        return math.sin(x)
    elif rule=='square':
        return x**2
    elif rule=='exp':
        return math.exp(x)
    else:
        return math.log(x)
def deri(rule,x):
    if rule=='sin':
        return math.cos(x)
    elif rule=='square':
        return 2*x
    elif rule=='exp':
        return math.exp(x)
    else:
        return 1/x
def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    val=x
    grad=1.0
    for i in reversed(functions):
        
        d=deri(i,val)
        val=func(i,val)
        grad=grad*d

    return grad
