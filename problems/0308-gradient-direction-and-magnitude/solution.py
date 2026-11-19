import numpy as np
import math
def gradient_direction_magnitude(gradient: list) -> dict:
    x=np.array(gradient)
    y=x**2
    mag=np.sqrt(np.sum(y))
    if not  np.any(x):
        return {
            'magnitude':0,'direction':np.zeros(len(gradient)),'descent_direction':np.zeros(len(gradient))
        }
    direc=x/mag
    return {
        'magnitude':mag,
        'direction':direc,
        'descent_direction':-1*direc
    }
