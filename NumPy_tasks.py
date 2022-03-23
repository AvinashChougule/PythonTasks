# NumPy Array creation
# Get the Dimention of Numpy array
# Shape of the array
# Get the data type of the array
# Change the data type of the array
# Get the size of the array elements and the array


# array1 = np.array([1,2,3,4])
# array2 = np.array([[1,2,3],[4,5,6],[6,7,8]])
# print(array1.ndim)
# print(array2)
# # it shows dimentions of the array
# print(array2.ndim)
#
# #it will show count of elements in dimention
# shape1 = np.shape([1,2,3,4,5])
# print(shape1)

# memory consumed size for array
# size = array2.itemsize
# print(size)

# elements = array2.nbytes
# print(elements)
import numpy as np

data = np.genfromtxt('E:/Python Data/example.txt')
print(data[data>50])







# to find diterminant using identity matrix and linear Ulzebra
# identity = np.identity(2)
# threeArray = np.full((3,3),3)
# determinant = np.linalg.det(identity)
# determinant2 = np.linalg.det(threeArray)
# print(determinant)
# print(determinant2)

# matrix multiplication using matmul() function
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# z = np.array([[2, 3], [4, 5], [6, 7]])
# f = np.matmul(x, z)
# print(f)
# 1 for single array, 2 for row , 4 for elements print zero (0)
# a = np.zeros((1, 2, 4), dtype =  'int32')
# a = np.ones((1,2,4), dtype =  'int32')
# a = np.full((1,2,4),99)
# a = np.random.rand(2,4)
# a = np.random.randint(5, size=(6, 4))
# a = np.random.randint(-4, 5, size=(6, 4))
# b = np.random.randint(5, size=(6, 4))
# c = np.random.random_sample(b.shape)
# z = a + a
# print(z)

# a = np.array3 = [[1, 2, 3, 4, 5, 6, 7],
#                  [11, 22, 33, 44, 55, 66, 77],
#                  [111, 222, 333, 444, 555, 666, 777]]
# # fetch specific element
# print(a[2][4])
# # fetch selected row
# print(a[1][:])

# fetch specific column
# print(a[:][1])
# print(a[0,0:6:2])
# a[1][2] = 44
# print(a)
