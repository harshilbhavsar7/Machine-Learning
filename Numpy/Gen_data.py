import numpy as np

# print(np.genfromtxt('data.txt',delimiter=','))

#boolean masking and advanced indexing

arr=np.genfromtxt('data.txt',delimiter=',')
arr=arr.astype('int32')
# print(arr)
# print(arr>50)
# print(arr[arr>50]) 
print(np.any(arr>50,axis=1))#axis 0 means columns wise and 1 means rows wise