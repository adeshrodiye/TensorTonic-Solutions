import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    A = np.array(v)
    N = len(A)
    B = np.zeros((N,N), dtype=A.dtype)

    ind = np.arange(N)

    B[ind,ind] = A[ind]
        
    return B