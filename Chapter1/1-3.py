import numpy as np

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

zero = np.zeros(5)

print("dim : ",zero.ndim)
print(f"unit vector : {unit_vector(zero)}\n")