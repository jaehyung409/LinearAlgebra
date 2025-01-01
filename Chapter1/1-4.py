import numpy as np
import matplotlib.pyplot as plt


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def vector_scalar(v, s):
    return v * s


vec1 = np.array([1, 2])
scalar = 5
unit_vec = unit_vector(vec1)
new_vec = vector_scalar(unit_vector(vec1), scalar)
plt.figure(figsize=(6, 6))
a1 = plt.arrow(0, 0, vec1[0], vec1[1], head_width=.3, width=.1, color='k', length_includes_head=True)
a2 = plt.arrow(0, 0, new_vec[0], new_vec[1], head_width=.3, width=.1, color=[.5, .5, .5], length_includes_head=True)
a3 = plt.arrow(0, 0, unit_vec[0], unit_vec[1], head_width=.3, width=.1, color=[.8, .8, .8], length_includes_head=True)
plt.legend([a1, a2, a3], ['v', '5*unit(v)', 'unit(v)'])
plt.title('Vectors v, 5*unit(v), and unit(v)')
plt.grid(linestyle='--', linewidth=.5)
plt.axis('square')
plt.axis([-6, 6, -6, 6])
plt.show()
