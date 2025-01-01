import numpy as np

def transpose(matrix):
    ret_matrix = []
    for i in matrix:
        ret_matrix.append(i)
    return np.array(ret_matrix)

matrix1 = np.random.randint(-10, 11, size=(1,3))
matrix1_T = np.transpose(matrix1)

print(f"matrix1 : \n{matrix1}\n, shape : {matrix1.shape}\n")
print(f"matrix1_T : \n{matrix1_T}\n, shape : {matrix1_T.shape}\n")
