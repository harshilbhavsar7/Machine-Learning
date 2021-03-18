import numpy as np

# b=np.zeros(2)
a=np.zeros((2,3,3,3))

# b=np.ones(2)

b=np.full((2,2),78,dtype="int32")

c=np.full_like(a,4)

# d=np.random.rand(3,2)
d=np.random.random_sample(c.shape)

e=np.random.randint(5,size=(4,4))

f=np.identity(2)

arr=np.array([[2,3,4]])
arr1=np.repeat(arr,5,axis=0	)
print(arr1)
