import numpy as np
import pandas as pd
from sklearn.datasets import make_regression

np.random.seed(0)
n_samples = 1000

X, y = make_regression(n_samples=n_samples, n_features=1, n_informative=1, noise=40, random_state=0)

print('X: ', X[:5])
print('y: ', y[:5])


# Scale X (years of experience) to 0..10 range
X = np.interp(X, (X.min(), X.max()), (0, 10))

# Scale y (salary) to 30000..100000 range
y = np.interp(y, (y.min(), y.max()), (30000, 100000))

# To dataframe
df = pd.DataFrame({'experience': X.flatten(), 'salary': y})
print(df.head(10))

from matplotlib import pyplot as plt

plt.scatter(X, y, color='blue', marker='.', label='Salary')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
