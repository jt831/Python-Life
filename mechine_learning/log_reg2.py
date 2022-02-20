import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.optimize import fmin_tnc
from sklearn.metrics import classification_report


def load_data(path):
    """
    读取格式为mat的数据

    :param path:
    :return:
    """
    data = loadmat(path)
    X = data['X']
    y = data['y'].flatten()
    return X, y


def plot_100_image(X):
    """
    随机打印数据集中100个数字

    :param X:
    :return:
    """
    sample_index = np.random.choice(np.array(X.shape[0]), 100)
    images = X[sample_index, :]

    fig, ax = plt.subplots(figsize=(8, 8), nrows=10, ncols=10, sharey='all', sharex='all')
    for i in range(10):
        for j in range(10):
            ax[i, j].matshow(images[i * 10 + j].reshape(20, 20), cmap='gray_r')

    plt.xticks([])
    plt.yticks([])
    plt.show()


def serialize(a, b):
    return np.r_[a.flatten(), b.flatten()]  # 合并数组；降维


def deserialize(seq):
    return seq[: 25 * 401].reshape(25, 401), seq[25 * 401:].reshape(10, 26)  # 恢复原来的维数


def expand_y(y):
    """
    将y从原来的1到10的数字变成一个【1 * 10】的数组，为什么不是0到9啊草
    比如1变成【1 0 0 0 0 0 0 0 0 0】
    :param y:
    :return:
    """
    result = []
    for i in y:
        y_array = np.zeros(10)
        y_array[i - 1] = 1
        result.append(y_array)

    return np.array(result)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def feed_forward(theta, X):
    t1, t2 = deserialize(theta)
    a1 = X
    z2 = a1 @ t1.T
    a2 = np.insert(sigmoid(z2), 0, 1, axis=1)
    z3 = a2 @ t2.T
    a3 = sigmoid(z3)
    cache = {'a1': a1,
             'z2': z2,
             'a2': a2,
             'z3': z3,
             'a3': a3}
    return cache


def cost(theta, X, y):
    cache = feed_forward(theta, X)
    a3 = cache['a3']

    J = -y * np.log(a3) - (1 - y) * np.log(1 - a3)
    return J.sum() / len(X)


def cost_Reg(theta, X, y, l):
    t1, t2 = deserialize(theta)
    reg = np.sum(t1[:, 1:] ** 2) + np.sum(t2[:, 1:] ** 2)
    return l / (2 * X.shape[0]) * reg + cost(theta, X, y)


def sigmoid_gradiant(z):
    """
    对sigmoid函数求导

    :param z:
    :return:
    """
    return sigmoid(z) * (1 - sigmoid(z))


def random_init(size):
    """
    随机初始化。从-0.12到0.12均匀地返回size个值

    :param size:
    :return:
    """
    return np.random.uniform(-0.12, 0.12, size)


def gradiant(theta, X, y):
    t1, t2 = deserialize(theta)
    cache = feed_forward(theta, X)
    a1 = cache['a1']
    z2 = cache['z2']
    a2 = cache['a2']
    z3 = cache['z3']
    a3 = cache['a3']

    d3 = a3 - y
    d2 = d3 @ t2[:, 1:] * sigmoid_gradiant(z2)
    D2 = d3.T @ a2
    D1 = d2.T @ a1
    D = (1 / X.shape[0]) * serialize(D1, D2)

    return D


# X的每一行代表一个手写数字的灰度值, y表示这一行的灰度值对应的数字
X, y = load_data('ex4data1.mat')
X = np.insert(X, 0, 1, axis=1)  # 插入全为1的列
y = expand_y(y)

data = loadmat('ex4weights.mat')
t1, t2 = data['Theta1'], data['Theta2']
theta = serialize(t1, t2)
cache = feed_forward(theta, X)

