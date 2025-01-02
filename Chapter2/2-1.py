import numpy as np

def linear_combination(scalars, vectors):
    ret_vec = []
    for (scalar, vector) in zip(scalars, vectors):
        ret_vec.append(scalar * vector)
    return np.array(ret_vec)

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])
scalars = [3, 2, 1]
print(linear_combination(scalars, [v1, v2, v3]))