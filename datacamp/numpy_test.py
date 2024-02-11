import numpy as np

# NumPy Creating Arrays
my_array1 = np.array([[1 , 2, 3],
                     [3, 4, 5],
                     [48, 4, 4]])

print(type(my_array1))
print(my_array1)
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("a = ", a.ndim)
print("b = ", b.ndim)
print("c = ", c.ndim)
print("d = ", d.ndim)
print("my_array1 = ", my_array1.ndim)

my_array2 = np.array([1, 2, 3, 4], ndmin=5)
print(my_array2)
print('number of dimensions: ', my_array2.ndim)


# NumPy Array Indexing
my_array3 = np.array([1, 2, 3])
print(my_array3[0])
print(my_array3[0] + my_array3[2])

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])
print('2nd element on 1st row: ', arr[0, 1])

print(arr[0:,0:])