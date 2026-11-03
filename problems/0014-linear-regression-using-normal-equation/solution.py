import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	#The normal form of the equation is: θ=((X^T X)^-1)(X^T)y
	X=np.array(X)
	y=np.array(y)
	theta=(np.linalg.inv(X.T @ X))@(X.T @y)
	return theta