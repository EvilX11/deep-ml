import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    m=len(batch_indices)
    xb=np.array(X[batch_indices])
    yb=np.array(y[batch_indices])
    
    error=xb@weights+bias-yb
    dw=(2/m)*(xb.T@error)
    db=(2/m)*np.sum(error)
    nw=weights-lr*dw
    nb=bias-lr*db 
    return np.append(nw,nb)
   