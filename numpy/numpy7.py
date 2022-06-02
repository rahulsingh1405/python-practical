import numpy as np
r,c = list(map(int,input("Enter the row and col : ").split()))
lst1 = list(map(int,input("Enter the element : ").split()))
arr1 = np.array([lst1]).reshape(r,c)
print(arr1)