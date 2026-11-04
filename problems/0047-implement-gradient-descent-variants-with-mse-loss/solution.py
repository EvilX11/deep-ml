import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # For SGD: wnew=wold-2a(wTxi-yi)xi
    m=X.shape[0] #number of samples
    if method=="stochastic":
        for j in range(n_epochs):
            for i in range(m):
                weights=weights-2*learning_rate*((weights.T@X[i]-y[i])*X[i])
    elif method=='batch':
        for j in range(n_epochs):
            weights=weights-((2*learning_rate*((X.T@(X@weights-y))))/m)
    else:
        for j in range(n_epochs):
            for start in range(0,m,batch_size):
                X_new=X[start:start+batch_size]
                Y_new=y[start:start+batch_size]
                weights=weights-(2*learning_rate*((X_new.T@(X_new@weights-Y_new))))/batch_size
                
    return weights
