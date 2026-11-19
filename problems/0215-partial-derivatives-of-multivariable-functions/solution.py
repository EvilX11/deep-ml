import numpy as np
import math
def deri(rule,x,y,z):
    if rule=='poly2d':
        return (2*x*y+y**2,x**2+2*x*y)
    elif rule=='exp_sum':
        return (math.exp(x+y),math.exp(x+y))
    elif rule=='product_sin':
        return (math.sin(y),x*math.cos(y))
    elif rule=='poly3d':
        return (2*x*y,x**2+z**2,2*z*y)
    else:
        return (2*(x-y),2*(x-y)*(-1))

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
    
    
    x,y,z=0,0,0
    x=point[0]
    y=point[1]
    if len(point)==3:
        z=point[2]
    val=deri(func_name,x,y,z)
    
    return val
    