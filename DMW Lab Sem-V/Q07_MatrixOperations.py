import numpy as np

matrix1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 7, 9]])

matrix2 = np.array([[7, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])

print("Matrix1 + Matrix2:")
print(matrix1 + matrix2)

print("\nMatrix1 - Matrix2:")
print(matrix1 - matrix2)

print("\nMatrix1 * Matrix2:")
print(np.dot(matrix1, matrix2))

print("\nMatrix1 / Matrix2 (element-wise division):")
print(matrix1 / matrix2)

print("\nInverse of Matrix1:")
print(np.linalg.inv(matrix1))

print("\nInverse of Matrix2:")
print(np.linalg.inv(matrix2))
