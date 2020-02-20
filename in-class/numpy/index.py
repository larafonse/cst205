import numpy as np

a = np.array([1,2,3],dtype='int16')
b = np.array([[1,2,3],[4,5,6]])

print(a)
print(b)

# Dimensions
print(a.ndim)
print(b.ndim)

# shape
print(a.shape)
print(b.shape)

# type
print(a.dtype)
print(b.dtype)

# number bytes
print(a.nbytes)
print(b.nbytes)

# accessing rows
print(b[1,1])

# specific row
print(b[:,1])
# colloms
print(b[1,:])