import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

    A=np.array(a)
    B=np.array(b)
    if(A.shape[1]!=B.shape[0]):
        return -1
    return np.matmul(A,B)