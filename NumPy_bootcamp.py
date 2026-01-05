import numpy as np

arr = np.array([10,20,30,40,50,60])

two_array = np.array([[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90],
                      [1, 2, 3]])
'''
print(arr)
print(two_array)

print(arr.shape) # (6,) that means 1D array
print(two_array.shape) # (4,3) that means 4 * 3 matrix

'''

print(arr.ndim)  # Dimension print korbe
print(two_array.ndim) 

print(np.mean(arr))  # mean() -> to find average
print(np.mean(two_array))
print(np.std(arr)) # to find Standard Deviation 

reshaped_arr = arr.reshape(2,3)
print(reshaped_arr.ndim) # Dimension 2
print(reshaped_arr.shape) # (2, 3)

matrix_1 = np.array([[10,20,30],
                     [40,50,60]])
matrix_2 = np.array([[10,30],
                     [20,40],
                     [30,50]])

multiplication = matrix_1.dot(matrix_2) # Matrix multiplication
print(multiplication)
