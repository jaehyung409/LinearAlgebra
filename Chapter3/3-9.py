import numpy as np
import matplotlib.pyplot as plt

def test_kmeans(dots, k):
    test_centroids = dots[np.random.choice(range(len(dots)), k, replace=False)]
    while True:
        test_labels = np.argmin(np.linalg.norm(dots[:, None] - test_centroids, axis=2), axis=1)
        new_centroids = np.array([dots[test_labels == i].mean(axis=0) for i in range(k)])
        if np.all(test_centroids == new_centroids):
            break
        test_centroids = new_centroids
    return test_labels, test_centroids

data = np.random.rand(150, 2)
for _ in range(8):
    labels, centroids = test_kmeans(data, _+1)
    colors = ["g.", "r.", "c.", "y.", "b.", "m.", "k.", "w."]
    for i in range(len(data)):
        plt.plot(data[i][0], data[i][1], colors[labels[i]], markersize=10)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5)
    plt.show()