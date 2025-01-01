import numpy as np
import matplotlib.pyplot as plt

def orthogonal_projection(vector_a, vector_b):
    return np.dot(vector_a, vector_b) / np.dot(vector_b, vector_b) * vector_b

def vector_orthogonal_depolarization(vector_a, vector_b):
    return vector_a - orthogonal_projection(vector_a, vector_b)

vector1 = np.random.randint(1, 6, size=2)
vector2 = np.random.randint(1, 6, size=2)
vector1_depolarization, vector1_projection = vector_orthogonal_depolarization(vector1, vector2), orthogonal_projection(vector1, vector2)
plt.figure(figsize=(6, 6))
a = plt.arrow(0, 0, vector1[0], vector1[1], head_width=.3, width=.1, color='k', length_includes_head=True)
b = plt.arrow(0, 0, vector2[0], vector2[1], head_width=.3, width=.1, color='b', length_includes_head=True)
depolarization = plt.arrow(0, 0, vector1_depolarization[0], vector1_depolarization[1], head_width=.3, width=.1, color='g', length_includes_head=True)
projection = plt.arrow(0, 0, vector1_projection[0], vector1_projection[1], head_width=.3, width=.1, color='r', length_includes_head=True)
plt.legend([a, b, depolarization, projection], ['vector1', 'vector2', 'vector1_depolarization', 'vector1_projection'])
plt.title('Orthogonal depolarization of vector1 onto vector2')
plt.grid(linestyle='--', linewidth=.5)
plt.axis('square')
plt.axis([-6, 6, -6, 6])
plt.show()