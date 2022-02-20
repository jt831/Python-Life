import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'ex1data2.txt'

data = pd.read_csv(path, header=None, names=['Size', 'Bedrooms', 'Price'])
data = (data - data.mean()) / data.std()  # 防止数据量级相差过大

data.insert(0, 'Ones', 1)

lines = data.shape[0]
cols = data.shape[1]

X = data.iloc[:, 0:cols - 1]
Y = data.iloc[:, cols - 1:cols]
theta = np.zeros((1, cols - 1))

X = np.array(X)
Y = np.array(Y)

assert (X.shape == (lines, cols - 1))
assert (Y.shape == (lines, 1))
assert (theta.shape == (1, cols - 1))


def cost_func(X, Y, theta):
    m = X.shape[0]
    inner = np.power((X.dot(theta.T) - Y), 2)
    cost = np.sum(inner) / (2 * m)

    return cost


def liner_regression(X, Y, theta, learning_rate=0.01, times=1000):
    m = X.shape[0]
    cost = np.zeros(times)

    for i in range(times):
        theta -= (learning_rate / m) * (X.dot(theta.T) - Y).T.dot(X)
        cost[i] = cost_func(X, Y, theta)

    return theta, cost


theta, cost2 = liner_regression(X, Y, theta, 0.01, 1000)


fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(np.arange(1000), cost2, color='red')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()

