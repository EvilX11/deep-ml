
import numpy as np

def rmse(y_true, y_pred):
    n=y_true.size
    if y_true.shape!=y_pred.shape or y_true.size==0:
        raise ValueError("Invalid Input")
    return np.sqrt(np.sum((y_true-y_pred)**2)/n)
