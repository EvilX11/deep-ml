import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	axis=1
	if mode=='column':
		axis=0
	
	m=np.array(matrix)
	means=np.mean(m,axis=axis)

	return means