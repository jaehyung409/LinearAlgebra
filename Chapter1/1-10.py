import numpy as np
import matplotlib.pyplot as plt

def orthogonal_projection(vector_a, vector_b):
    return np.dot(vector_a, vector_b) / np.dot(vector_b, vector_b) * vector_b

def wrong_orthogonal_projection(vector_a, vector_b):
    return np.dot(vector_a, vector_b) / np.dot(vector_a, vector_a) * vector_b

def sanity_check(vector_a, vector_b):
    projection_vector = orthogonal_projection(vector_a, vector_b)
    wrong_projection_vector = wrong_orthogonal_projection(vector_a, vector_b)
    if np.array_equal(projection_vector, wrong_projection_vector):
        print("CORRECT !")
    else:
        print(f"correct projection : {projection_vector}\nwrong projection : {wrong_projection_vector}")
        print(f"difference : {projection_vector / wrong_projection_vector}")
        print(f"because of the difference (dot product difference), {vector_a.dot(vector_a)} != {vector_b.dot(vector_b)}")
        print("WRONG !")

vector_a = np.array([2, 6]) # dot product = 40
vector_b = np.array([3, 1]) # dot product = 10
sanity_check(vector_a, vector_b)
plt.figure(figsize=(6, 6))
a = plt.arrow(0, 0, vector_a[0], vector_a[1], head_width=.3, width=.1, color='k', length_includes_head=True)
b = plt.arrow(0, 0, vector_b[0], vector_b[1], head_width=.3, width=.1, color='b', length_includes_head=True)
projection_vector = orthogonal_projection(vector_a, vector_b)
wrong_projection_vector = wrong_orthogonal_projection(vector_a, vector_b)
plt.arrow(0, 0, projection_vector[0], projection_vector[1], head_width=.3, width=.1, color='r', length_includes_head=True)
plt.arrow(0, 0, wrong_projection_vector[0], wrong_projection_vector[1], head_width=.3, width=.1, color='g', length_includes_head=True)
plt.legend([a, b], ['vector_a', 'vector_b'])
plt.title('Orthogonal projection of vector_a onto vector_b')
plt.grid(linestyle='--', linewidth=.5)
plt.axis('square')
plt.axis([-6, 6, -6, 6])
plt.show()