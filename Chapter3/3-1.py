import numpy as np


def pearson(a, b):
    normal_a = a - np.mean(a)
    normal_b = b - np.mean(b)
    return np.sum(normal_a * normal_b) / (np.sqrt(np.dot(normal_a, normal_a)) * np.sqrt(np.dot(normal_b, normal_b)))

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.sqrt(np.dot(a, a)) * np.sqrt(np.dot(b, b)))

def pearson_corrcoef(a, b):
    return np.corrcoef(a, b)[0, 1]


vec1 = np.array([0, 1, 2, 3])
vec2 = np.array([0, 2, 6, 9])
print("----------pearson----------")
print(pearson(vec1, vec2))
print(pearson_corrcoef(vec1, vec2))
print("-----cosine_similarity-----")
print(cosine_similarity(vec1, vec2))