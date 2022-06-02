import numpy as np
r = int(input("Enter the row of matrix 1 : "))
c = int(input("Enter the col of matrix : "))
m1 = []
for i in range(r):
    a = []
    for j in range(c):
        ele = int(input("Enter the element of m1 matrix : "))
        a.append(ele)
    m1.append(a)
n = int(input("Enter the row of matrix 2 : "))
m = int(input("Enter the col of matrix 2 : "))
m2 = []
for i in range(n):
    p = []
    for j in range(m):
        ele1 = int(input("Enter the element of m2 matrix: "))
        p.append(ele)
    m2.append(p)
arr1 = np.array(m1)
arr2 = np.array(m2)
p = np.add(arr1,arr2)
print(p)
q = np.subtract(arr1,arr2)
print(q)
r = np.multiply(arr1,arr2)
print(r)
s = np.divide(arr1,arr2)
print(s)
t = np.mod(arr1,arr2)
print(t)
u = np.power(arr1,arr2)
print(u)