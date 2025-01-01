import numpy as np
import math

def norm(vector):
    num = 0
    #for i in range(len(vector.flatten())):
    #    num += math.pow(vector.flatten()[i],2)
    num = np.sum(vector ** 2)
    return math.sqrt(num)

dim1 = [np.random.randint(-10, 11, size=5) for _ in range(0, 20)]
dim2 = [np.random.randint(-10, 11, size=(3,3)) for _ in range(0, 20)]
dim3 = [np.random.randint(-10, 11, size=(2,2,3)) for _ in range(0, 20)]

for dim in dim1,dim2,dim3:
    for vector in dim:
        if norm(vector) == np.linalg.norm(vector):
            continue
        else:
            print(f"wrong case : {vector}\nyour : {norm(vector)}\nanswer : {np.linalg.norm(vector)}")

print("FINISH !")