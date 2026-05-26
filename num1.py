import numpy as np

#print(np.__version__)
arr= np.array([12,12,13])
print(arr)
print("Sum:",np.sum(arr))
print("mean:",np.mean(arr))

a= np.array([[[39,90]]])
print(a.ndim)
print(a.shape)