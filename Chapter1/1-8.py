import numpy as np
import matplotlib.pyplot as plt

def orthogonal_projection(vector_a, vector_b):
    return np.dot(vector_a, vector_b) / np.dot(vector_b, vector_b) * vector_b

vector_a = np.array([2, 6])
vector_b = np.array([3, 1])
projection_vector = orthogonal_projection(vector_b, vector_a)
vector_beta = projection_vector - vector_b
plt.figure(figsize=(6, 6))
a = plt.arrow(0, 0, vector_a[0], vector_a[1], head_width=.3, width=.1, color='k', length_includes_head=True)
b = plt.arrow(0, 0, vector_b[0], vector_b[1], head_width=.3, width=.1, color='b', length_includes_head=True)
beta = plt.arrow(vector_b[0], vector_b[1], vector_beta[0], vector_beta[1], linestyle = '--', head_width=.3, width=.1, color='g', length_includes_head=True)
proj = plt.arrow(0, 0, projection_vector[0], projection_vector[1], head_width=.3, width=.1, color='r', length_includes_head=True)
plt.legend([a, b, proj], ['vector_a', 'vector_b', 'projection_vector'])
plt.title('Orthogonal projection of vector_a onto vector_b')
plt.grid(linestyle='--', linewidth=.5)
plt.axis('square')
plt.axis([-6, 6, -6, 6])
plt.show()