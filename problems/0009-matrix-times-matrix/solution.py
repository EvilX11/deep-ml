import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    A=np.array(a)
    B=np.array(b)
    if(A.shape[1]!=B.shape[0]):
        return -1
    result=[]
    for i in range(A.shape[0]):
        r=[]
        for j in range(B.shape[1]):
            r.append(np.sum(A[i]*B[:,j]))
        result.append(r)
    return result