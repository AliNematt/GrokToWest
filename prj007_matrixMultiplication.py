import numpy as np
def arrayMP(myArray1, myArray2) : return np.dot(myArray1,myArray2)

myArray1 = np.array([[1, 2], [2, 4]])
myArray2 = np.array([[5, 9], [1, 35]])
print(arrayMP(myArray1, myArray2))