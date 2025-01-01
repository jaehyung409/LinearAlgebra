import numpy as np

def vector_dot_product_ab(a, b):
    return matrix_dot_product(a, b)

def matrix_dot_product_ba(a, b):
    return matrix_dot_product(b, a)

def matrix_dot_product(a, b):
    row_vec = len(a)
    col_vec = len(b[0])
    ret_vec = np.zeros((row_vec, col_vec))

    for i in range(row_vec):
        for j in range(col_vec):
            for k in range(len(b)):
                ret_vec[i][j] += a[i][k] * b[k][j]
    return ret_vec

matrix1 = np.random.randint(-10, 11, size=(3,3))
matrix2 = np.random.randint(-10, 11, size=(3,3))
print(f"matrix1 : \n{matrix1}\n")
print(f"matrix2 : \n{matrix2}\n")
print(f"vector_dot_product_ab : \n{vector_dot_product_ab(matrix1, matrix2)}\n")
print(f"matrix_dot_product_ba : \n{matrix_dot_product_ba(matrix2, matrix1)}\n")
if np.array_equal(vector_dot_product_ab(matrix1, matrix2), matrix_dot_product_ba(matrix2, matrix1)):
    print("vector_dot_product_ab == matrix_dot_product_ba")
else:
    print("vector_dot_product_ab != matrix_dot_product_ba")
print("FINISH !")