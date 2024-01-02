import numpy as np

# a= np.array([1,2,2,3,4])

# print(a)

# print (type(a))

# print(a.dtype)


# b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# print(b)
# print(b.dtype)

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# arr2=np.array([1,2,3,4,5,6,7])
# # print(arr[1:5])
# select = [1,3,4]
# d = arr[select]
# print(d)

# sum= np.add(arr,arr2)
# print(sum)


# c=np.subtract(arr,arr2)
# print(c)


# z=np.multiply(arr,arr2)
# print(z)

# d=np.divide(arr,arr2)
# print(d)

# dott=np.dot(arr,arr2)
# print(dott)

# f=arr+1
# print(f)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y)
print(Z)