import numpy as np
import matplotlib.pyplot as plt

def pearson(a, b):
    normal_a = a - np.mean(a)
    normal_b = b - np.mean(b)
    return np.sum(normal_a * normal_b) / (np.sqrt(np.dot(normal_a, normal_a)) * np.sqrt(np.dot(normal_b, normal_b)))

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.sqrt(np.dot(a, a)) * np.sqrt(np.dot(b, b)))

vector1 = np.array([0, 1, 2, 3])
pearson_array = []
cosine_array = []
for i in range(-50,50):
    vector2 = vector1 + i
    pearson_array.append(pearson(vector1, vector2))
    cosine_array.append(cosine_similarity(vector1, vector2))

plt.plot(range(-50,50), pearson_array, label="pearson")
plt.plot(range(-50,50), cosine_array, label="cosine")
plt.legend()
plt.show()