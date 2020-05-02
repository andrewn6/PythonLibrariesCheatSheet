import numpy as np

# Numpy Basic Commands

# Make an array
a = np.array([1, 2, 3])
print(a)

print("\n")

# Make a 2D Array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

print("\n")

# Get Dimension of an array
print(a.ndim)
print(b.ndim)

print("\n")

# Get Shape of an array
print(a.shape)
print(b.shape)

print("\n")

# Get Data Type
print(a.dtype)
print(b.dtype)

print("\n")

# Set a data type for an array
a = np.array([1, 2, 3], dtype='int16')
print(a.dtype)

print("\n")

# Get memory size (Bytes of each integer ele)
print(a.itemsize)

print("\n")

# Get total memory size of a array(Bytes of each element(added))
print(a.nbytes)

print("\n")

# Get size of an array (counts each element)
print(a.size)
print(b.size)

print("\n" * 2)

#############################################

# Accessing/Changing Specific Elements,Rows,Col.
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

print("\n")

# Get a specific element - array[row, col]
print(a[0, 3])
print(a[0, -4])


print("\n")

# Get a specific row - : like list slicing
print(a[0, :])

print("\n")

# Get a specific column
print(a[:, 3])

print("\n")

# Getting a little fancy array[row, startindex:endindex:steps]
print(a[0, 1:6:2])

print("\n")

# Changing a element
a[1, 5] = 20
print(a)

print("\n")

# Changing an entire column with the same element
a[:, 6] = 5
print(a)

print("\n")

# Changing an entire column with different element
a[:, 3] = [90, 100]
print(a)

print("\n")

# 3-Dimensional Arrays

# Make a 3D Array
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a)
print(a.ndim)  # Proof that it is a 3D Array

print("\n")

# Get Specific Element array[box(group of list), row, column]
print(a[0, 1, 1])
print(a[:, 1, :])

print("\n")

# Replacing is the same
a[:, 1, :] = [[90, 95], [100, 105]]
print(a)

print("\n")

##############################################

# Initializing different types of arrays


# All 0s Matrix - np.zeros(shape),it's float by default
print(np.zeros(5))  # 1D
print("\n")
print(np.zeros((2, 3)))  # 2D
print("\n")
print(np.zeros((2, 3, 3)))  # 3D

print("\n")

# All 1s Matrix -np.ones(shape)
onesMatrix = np.ones((3, 3, 3))
print(onesMatrix)

print("\n")

# To remove the float
onesMatrix = np.ones((3, 3, 3), dtype='int')
print(onesMatrix)

print("\n")

# Get a matrix of any number np.full((shape), num)
anyNumMatrix = np.full((3, 3), 6)
print(anyNumMatrix)

print("\n")

# Any Number using another array's shape np.full_like(array, num)
print(np.full_like(a, 99))

print("\n")

# Random decimal number - np.random.rand(shape)
print(np.random.rand(4, 2))
print("\n")
print(np.random.random_sample(a.shape))

print("\n")

# Random Integer Number np.random.randint(num, size=(shape))
print(np.random.randint(6, size=(3, 3)))
print("\n")
print(np.random.randint(1, 10, size=(3, 3)))

print("\n")

# Identity Matrix
print(np.identity(5))

print("\n")

# Repeat an array - np.repeat(array, howManyTimes, axis=0ifVertical or
# 1ifHorizontal)
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

print("\n")

# Making a simple matrix pattern
output = np.ones((5, 5))
print(output)
z = np.zeros((3, 3))
z[1, 1] = 9
print("\n")
print(z)
output[1:4, 1:4] = z
print("\n")
print(output)

print("\n")
# Be careful when copying arrays

# Making two varables the same - not copying
a = np.array([1, 2, 3])
b = a
b[0] = 1000
print(b)
print(a)

print("\n")

# Do this when copying a array to another variable - to not change the
# source or reference variable
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 1000
print(b)
print(a)

print("\n")

##############################################

# Mathematics

# Addition
a = np.array([1, 2, 3, 4])
print(a + 1)

print("\n")

# Subtraction
b = np.array([5, 6, 7, 8])
print(b - a)  # Subtracts it column by column(element-wise)

print("\n")

# Multiplication
print(a * b)

print("\n")

# Division
print(b / a)

print("\n")

# Exponetation
print(a**2)

print("\n")

# Take the cos and sin value
print(np.cos(a))
print(np.sin(a))


# Linear Algebra

# Matrices Multiplication
a = np.ones((2, 3))
print(a)
b = np.full((3, 2), 2)
print(b)
print(np.matmul(a, b))

print("\n")

# Find the determinant
a = np.identity(5)
print(np.linalg.det(a))

print("\n")

# Statistics

# Get Minimum
stats = np.array([[1, 2, 3], [4, 5, 6]])
print(np.min(stats))
print(np.min(stats, axis=1))  # Return min of each row
print(np.min(stats, axis=0))  # Return min of each column

print("\n")

# Get Maximum
print(np.max(stats))
print(np.max(stats, axis=1))
print(np.max(stats, axis=0))

print("\n")

# Get sum of array (can use axis too - 1=Row 0= Column)
print(np.sum(stats))
print(np.sum(stats, axis=1))
print(np.sum(stats, axis=0))

print("\n")

##############################################

# Reorganizing Arrays

# Reshaping Arrays array.reshape(row,column)
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before, "\n")
after = before.reshape(8, 1)
print(after, "\n")
# Even a 3D, as long as it is the same value
after3D = before.reshape(2, 2, 2)
print(after3D, "\n")


# Vertically Stacking Matrices/Vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(np.vstack([v1, v2]))
print(np.vstack([v1, v2, v2, v1]))  # Can pass the same vector

print("\n")

# Horizontally Stacking
h1 = np.ones([2, 4])
h2 = np.zeros([2, 2])
print(np.hstack((h1, h2)))

print("\n")

############################################

# Miscellaneous

# Generate from text file (.txt)
a = np.genfromtxt('data.txt', delimiter=',')
print(a)
b = a.astype('int32')  # copies all data then turns into what type you put in
print(b)

print("\n")
# Boolean Masking and Advanced Indexing

# Boolean Masking
print(a > 50)
print(a[a > 50])  # Indexing all data greater than 50

print("\n")

# Index with a list in numpy arrays
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a[[1, 2, 8]]  # assigning indices 1,2 and 8 to b
print(b)

print("\n")

# Using range to make a array then reshaping it
a = np.arange(1, 31)
a = a.reshape(6, 5)
print(a)
print(a[[0, 4, 5], 3:])
print(a[[0, 1, 2, 3], [1, 2, 3, 4]])
