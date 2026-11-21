import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    # n = len(x)
    # result = 0
    # for i in range(n):
    #     result += x[i] * y[i]
    # result=float(result)
    x = np.array(x,dtype=float)
    y =np.array(y,dtype=float)

    res = np.dot(x,y)

    return float(res)