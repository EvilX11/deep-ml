import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A=np.array(A)
	B=np.array(T)
	S=np.array(S)

	if np.linalg.det(T)==0 or np.linalg.det(S)==0:
		return -1
	
	T_inv=np.linalg.inv(T)
	trans=T_inv@A@S
	return trans