import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s'%(a.ndim, a.shape, a.dtype))

a = np.array([1,2,3,4,5,6,7,8])

a = a.reshape([2,4])

a = a.reshape([2,2,2])

x = np.array([[1,2,3],[4,5,6]], np.int32)

a = np.zeros([2,3])

np.random.random((2,3))

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

a = np.arange(10)
moving_average(a, 4)

a = np.arange(6)

csum = np.cumsum(a)