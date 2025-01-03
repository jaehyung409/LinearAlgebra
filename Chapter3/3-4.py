import numpy as np
import scipy.stats as stats
import time

def pearson(a, b):
    normal_a = a - np.mean(a)
    normal_b = b - np.mean(b)
    return np.sum(normal_a * normal_b) / (np.sqrt(np.dot(normal_a, normal_a)) * np.sqrt(np.dot(normal_b, normal_b)))

def pearson_performance_test(n):
    # 시간 측정을 위한 코드
    start_time = time.time()
    for _ in range(n):
        vector1 = np.random.rand(500)
        vector2 = np.random.rand(500)
        pearson(vector1, vector2)
    end_time = time.time()
    custom_pearson_time = end_time - start_time
    print("Custom Pearson time: ", custom_pearson_time)
    start_time = time.time()
    for _ in range(n):
        vector1 = np.random.rand(500)
        vector2 = np.random.rand(500)
        stats.pearsonr(vector1, vector2)
    end_time = time.time()
    scipy_pearson_time = end_time - start_time
    print("Scipy Pearson time: ", scipy_pearson_time)
    start_time = time.time()
    for _ in range(n):
        vector1 = np.random.rand(500)
        vector2 = np.random.rand(500)
        np.corrcoef(vector1, vector2)
    end_time = time.time()
    numpy_pearson_time = end_time - start_time
    print("Numpy Pearson time: ", numpy_pearson_time)
    return custom_pearson_time / scipy_pearson_time, custom_pearson_time / numpy_pearson_time

print(pearson_performance_test(1000))