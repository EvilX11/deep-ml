import numpy as np
import math 
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a=np.array(matrix)
	trace=a[0][0]+a[1][1]
	det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
	e1=(trace+math.sqrt(trace**2-(4*det)))/2.0
	e2=(trace-math.sqrt(trace**2-(4*det)))/2.0
	eigenvalues=[e1,e2]
	return eigenvalues