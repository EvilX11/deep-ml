import numpy as np

def bincount(a: np.ndarray, n_bins: int) -> np.ndarray:
    mpp={}
    for i in range(len(a)):
        mpp[a[i]]=mpp.get(a[i],0)+1
    l=[0]*n_bins
    for i in range(len(a)):
        l[a[i]]=mpp[a[i]]
    return l