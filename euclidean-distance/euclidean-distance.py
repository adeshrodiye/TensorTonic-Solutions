import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here

    x = np.asarray(x, dtype = float)
    y = np.asarray(y, dtype = float)

    res = np.sqrt(((x-y)**2).sum())

    return float(res)