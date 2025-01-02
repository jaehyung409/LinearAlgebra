import numpy as np

def linear_combination(scalars, vectors):
    ret_vec = []
    for (scalar, vector) in zip(scalars, vectors):
        ret_vec.append(scalar * vector)
    return np.array(ret_vec)

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
vec3 = np.array([7, 8, 9])
vec4 = np.array([10, 11, 12])
scalars = [5, 4, 3, 2, 1]
print(linear_combination(scalars, [vec1, vec2, vec3, vec4]))
scalars = [1, 2, 3]
print(linear_combination(scalars, [vec1, vec2, vec3, vec4]))