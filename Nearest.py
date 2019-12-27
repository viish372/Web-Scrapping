import numpy as np
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

array = np.random.random(20)
value =10
print(find_nearest(array, value))
print(array)
