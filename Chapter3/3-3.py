import scipy.stats as stats
import numpy as np


def pearsonr(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    std_x = np.std(x, ddof=1)
    std_y = np.std(y, ddof=1)
    covariance = np.sum((x - mean_x) * (y - mean_y)) / (len(x) - 1)
    correlation = covariance / (std_x * std_y)
    t_stat = correlation * np.sqrt(len(x) - 2) / np.sqrt(1 - correlation ** 2)
    p_value = stats.t.sf(np.abs(t_stat), df=len(x)-2) * 2
    return correlation, p_value

vector1 = np.array([0, 1, 2, 3])
vector2 = np.array([0, 2, 6, 9])
print("----------pearson----------")
print(pearsonr(vector1, vector2))
print("---------pearsonr----------")
print(stats.pearsonr(vector1, vector2))