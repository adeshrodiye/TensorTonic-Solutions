import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """

    N = len(A)
    M = len(A[0])

    a = np.empty((M,N))
    
    for i in range(0,N):
        for j in range(0,M):
            a[j][i] = A[i][j]
    return a

