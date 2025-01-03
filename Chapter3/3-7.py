import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))

# kernel (high-pass filter)
plt.subplot(2, 2, 1)
kernel = np.array([0, .1, .3, .8, -1, .8, .3, .1, 0])
kernel = kernel / np.sum(kernel)
x = np.arange(9)
plt.axis([-1, 100, -0.05, 0.35])
plt.plot(x, kernel, 'ks-')
plt.title('Kernel, High-pass filter')

# clock signal
plt.subplot(2, 2, 2)
x2 = np.arange(100)
# gaussian noise
y2 = np.random.normal(0, 0.1, 100)
plt.axis([-1, 100, -0.5, 0.5])
plt.plot(x2, y2, 'ks-')
plt.title('Gaussian Noise')

# convolution
plt.subplot(2, 2, 3)
length = len(x2)
y3 = np.zeros(length)
for i in range(4, length - 4):
    y3[i] = np.dot(kernel, y2[i - 4:i + 5])
plt.axis([-1, 100, -0.5, 0.5])
plt.plot(x2, y3, 'bs-')
plt.plot(x2, y2, 'ks-')
plt.title('Convolution')

plt.subplot(2, 2, 4)
plt.axis([-1, 100, -0.5, 0.5])
plt.plot(x2, y3, 'bs-')
plt.title('Convolution')

plt.show()