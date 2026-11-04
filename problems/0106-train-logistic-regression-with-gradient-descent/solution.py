import numpy as np
def sigmoid(z):
	return (1/(1+np.exp(-z)))
def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
	"""
	Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
	"""
	m,n = X.shape
	y=y.reshape(-1,1)
	theta=np.zeros((n+1,1))
	loss=[]
	X_new=np.insert(X,0,1,axis=1)
	for i in range(iterations):
		y_i=sigmoid(X_new@theta)
		loss_i=-np.sum(y*np.log(y_i)+(1-y)*np.log(1-y_i))
		loss.append(loss_i)
		gradient=X_new.T@(y_i-y)
		theta=theta-learning_rate*gradient

	theta=[round(float(x),4) for x in theta.flatten()]
	loss=[round(float(x),4) for x in loss]
	return (theta,loss)