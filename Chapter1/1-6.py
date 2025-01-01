import numpy as np

def vector_square_norm(vector):
    return np.sum(vector ** 2)

def vector_self_dot_product(vector):
    return np.dot(vector, vector)

vec1 = np.random.randint(-10, 11, size=5)
vec2 = np.random.randint(-10, 11, size=5)
vec3 = np.random.randint(-10, 11, size=5)

for vec in vec1, vec2, vec3:
    if vector_square_norm(vec) == vector_self_dot_product(vec):
        continue
    else:
        print(f"wrong case : {vec}\nyour : {vector_square_norm(vec)}\nanswer : {vector_self_dot_product(vec)}")

print("FINISH !")