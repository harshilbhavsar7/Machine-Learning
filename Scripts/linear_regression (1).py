# Reference link: https://medium.com/sigmoid/linear-regression-from-scratch-with-python-5c33712a1cec
# Simple linear regression from scratch using python

import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# We can use sklearn.linear_model to do the thing, but that will not help in learning the intusion.
# So we will use not use any library function.

'''
numpy -> for vectorized numeriacal computation on the dataset and algorithms.
matplotlib -> for graphical representation and plotting visual data.
sklearn.dataset -> To generate train and test dataset. 
'''

# Try to change feature size and you will an error: 'ValueError: x and y must be the same size'
# Add change y from row vector to column vector before increasing the size of features in the database.
# *****Try to implement this also after completing this part.
X, y = make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)

# print('X: ', X[:5])
# print('y: ', y[:5])

'''
Steps:
	- Randomly initialize parameters for the hypothesis function
	- Computing the mean squared error
	- Computing partial derivatives
	- Updating the parameters based on the derivatives and the learning rate
	- Repeat the process until the error is minimized (when global minima is reached)
	- Test on new dataset
'''

# Hypothesis function
'''
A linear equation is a standard form of straight line.
=> y = mx + c

We will use it as: h(x) = theta1*x1 + theta0,
where m and c are represented as parameters theta1 and theta0 respectively.
'''

def hypothesis(theta0, theta1, x):
	return theta0 + (theta1*x)

# ************We are not using activation function here as this is a linear regression function.
# We will use activation function only in Non-linear regression, Classification, logistic regression and other algorithms where output range has to be changed to the output.
'''
For example, here we need output in the range similar to y.
This can be for example: 1.2474, 7.54687 or etc which is similar to data in y(target).

But for example we need the output value in range of [0, 1], we will use Sigmoid function as our Activation function.
And if we want our output only in (0,1) binomial form, we will use Logistic function as our Actication function.
'''

'''
We activation, we would be rather taking about Generalized linear models(Logistic regression).
Linear regression also means, we are using square loss and no regularization.
So basically we define linear regression for continuous outputs.
'''

'''
Now the difference between Neural Network and Linear Regression is:
	- In Neural Network: We have multiple input x0, x1, x2, ....xn and single output y.
						We also have hidden layer between input and output nodes which carries weights with it.

	- In Linear Regression: We donot have hidden layer and thus we donot require any weights in it.
							Instead we have hypothesis function to get our output.
'''

# In the beginning, we randomly initialize our parameters, which means we give theta0 and theta1 random values/

# Creating initial plot
# def initalPlot(theta0, theta1, X, y):
max_x = np.max(X) + 100
min_x = np.min(X) - 100

xplot = np.linspace(min_x, max_x, 1000)
yplot = 1 + 1*xplot

plt.ion()	# Turn on interactive mode

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(xplot, yplot, color='#ff0000', label='Regression Line')
ax.scatter(X, y)
ax.axis([-10, 10, 0, 200])
fig.canvas.draw()

# Display the graph
def plotLine(theta0, theta1, X, y):

	max_x = np.max(X) + 100
	min_x = np.min(X) - 100

	xplot = np.linspace(min_x, max_x, 1000)
	yplot = theta0 + theta1*xplot

	plt.plot(xplot, yplot, color='#ff0000', label='Regression Line')

	plt.scatter(X, y)
	plt.axis([-10, 10, 0, 200])
	plt.show()


def updatePlot(theta0, theta1, X, y):
	yplot = theta0 + theta1*xplot

	line1.set_ydata(yplot)
	fig.canvas.draw()

# theta0 = np.random.rand()
# theta1 = np.random.rand()

# plotLine(theta0, theta1, X, y)

# Clearly the line is wrong

# Error Function
'''
	- Find how far it is from actual points: Substract actual value y from predicted value h(x)
	- Make sure the error is positive all the time (we don't want it negative).
	- M is the number of points (data) in our dataset. We repeat this substraction and squaring for all m points
	- Finally we divide this error by 2. This will help later in updating the parameter.
'''

def cost(theta0, theta1, X, y):
	costValue = 0
	for (xi, yi) in zip(X, y):
		costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
	costValue = costValue/len(X)
	return costValue

# Now we have value for how wrong our function is. We need to adjust the function to reduce this error.

# Calculating Derivatives
'''
Our goal with linear regression is to find the line which best fits a set of data points. That is, it must have the lowest error.

We will graph our cost function. This process is called as minimizing the cost function.
# To minimize the cost, we will bring our gradient to near zero.
'''

# Gradient descent
def derivatives(theta0, theta1, X, y):
	dtheta0 = 0
	dtheta1 = 0
	for (xi, yi) in zip(X, y):
		dtheta0 += hypothesis(theta0, theta1, xi) - yi	# Derivation of Cost with respect to theta0
		dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi	# Derivative of Cost with respect to theta1

		dtheta0 = dtheta0/len(X)
		dtheta1 = dtheta1/len(X)

		return dtheta0, dtheta1

# Updating the parameters based on the 'Learning Rate':
# Alpha is the learning rate, which allows the parameters to update by small amount.


def updateParameters(theta0, theta1, X, y, alpha):
	dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
	theta0 = theta0 - (alpha*dtheta0)
	theta1 = theta1 - (alpha*dtheta1)

	return theta0, theta1

# Minimizing cost function
# Calculate derivatives, and updating the weights until the error is as low as possible.

def LinearRegression(X, y):
	theta0 = np.random.rand()
	theta1 = np.random.rand()

	# initalPlot(theta0, theta1, X, y)
	for i in range(1, 100000):
		if i % 1000 == 0:
			# plotLine(theta0, theta1, X, y)
			updatePlot(theta0, theta1, X, y)
		print(i,'>',cost(theta0, theta1, X, y))
		theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)

LinearRegression(X, y)

'''
As we can see here that, when we have smaller learning rate, the process(training) gets stuck without generalizing completely.
And if we keep the learning rate large, the model converges too quickly to a suboptimal solution.
'''