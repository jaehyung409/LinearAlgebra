import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))

# kernel
plt.subplot(2, 2, 1)
kernel = np.array([-1,2])
x=np.array([15,16])

plt.axis([-1,30,-1.25,2.25])

plt.plot(x, kernel, 'ks-',)
plt.title('Kernel')

# clock signal
plt.subplot(2, 2, 2)
x2=np.arange(30)
y2=np.zeros(30)
y2[10:20]=1
plt.axis([-1,30,-0.25,1.25])
plt.plot(x2, y2, 'ks-')
plt.title('Clock Signal')

# convolution
plt.subplot(2, 2, 3)
length = len(x2)
y3 = np.zeros(length)
for i in range(1,length-1):
    y3[i] = np.dot(kernel, y2[i-1:i+1])
plt.axis([-1,30,-1.25,2.25])
plt.plot(x2, y3, 'bs-')
plt.plot(x2, y2, 'ks-')
plt.title('Convolution')

plt.show()