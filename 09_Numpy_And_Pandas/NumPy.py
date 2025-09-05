# Numpy Assignments

# Exercise 1: Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Array:")
print(arr)
print("\nndim (Number of dimensions):", arr.ndim)
print("shape (Rows, Columns):", arr.shape)
print("\nSlicing Examples:")
print("First row:", arr[0])
print("First column:", arr[:, 0])
print("Element at row 2, col 3:", arr[1, 2])
print("First 2x2 subarray:\n", arr[0:2, 0:2])
print("Last row:", arr[-1])
print("Last column:", arr[:, -1])


# Exercise 2 : Create one dimensional array and perform ndim, shape, reshape operation on it.

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print("Array:")
print(arr)
print("\nndim (Number of dimensions):", arr.ndim)
print("shape:", arr.shape)
reshaped_2d = arr.reshape(2, 3)
print("\nReshaped into 2x3:\n", reshaped_2d)
reshaped_3d = arr.reshape(2, 1, 3)
print("\nReshaped into 3D (2x1x3):\n", reshaped_3d)
