import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    X = np.asarray(x, dtype = float)
    Y = np.asarray(y, dtype = float)
    res = 0
    for i in range(len(X)):
        res += np.abs(X[i]-Y[i]).sum()

    return res