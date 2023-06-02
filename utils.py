import numpy as np

def per_layer_multiply(a: np.ndarray, b: np.ndarray):
    return np.array([i @ j for i, j in zip(a, b)])


def comparator(a: np.ndarray):
    return np.diag(a[:,0] ** -1)
