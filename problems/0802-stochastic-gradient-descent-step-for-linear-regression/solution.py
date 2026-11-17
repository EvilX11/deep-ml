import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    m,n=X.shape
    for ind in range(n_iter):
        i=ind%m
        x_iter=X[i]
        y_iter=y[i]
        grad=2*(weights@x_iter-y_iter)*x_iter
        weights=weights-learning_rate*grad
            
    return weights.tolist()
