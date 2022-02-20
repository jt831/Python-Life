import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.optimize as opt

path = 'ex5data1.mat'
data = loadmat(path)

# Training Set
X, y = data['X'], data['y']
# Cross validation Set
Xval, yval = data['Xval'], data['yval']
# Test Set
Xtest, ytest = data['Xtest'], data['ytest']
# Insert a colum of '1'
X = np.insert(X, 0, 1, axis=1)
Xval = np.insert(Xval, 0, 1, axis=1)
Xtest = np.insert(Xtest, 0, 1, axis=1)


def plot_data():
    plt.figure(figsize=(8, 5))
    plt.scatter(X[:, 1], y, c='r', marker='x')
    plt.xlabel('Change in water level')
    plt.ylabel('Water flowing out of the dam')
    plt.grid(True)


def costReg(theta, X, y, l=1):
    cost = ((X @ theta - y.flatten()) ** 2).sum()
    regterm = l * (theta[1:] @ theta[1:])
    return (cost + regterm) / (2 * X.shape[0])


theta = np.ones(X.shape[1])


def gradientReg(theta, X, y, l=1):
    grad = (X @ theta - y.flatten()) @ X
    regterm = l * theta
    regterm[0] = 0
    return (grad + regterm) / X.shape[0]


def trainLinerReg(X, y, l=1):
    theta = np.zeros(X.shape[1])
    res = opt.fmin_tnc(func=costReg, x0=theta, fprime=gradientReg, args=(X, y, l))
    return res[0]


def plot_learning_curve(X, y, Xval, yval, l=0):
    """
    观察训练集代价和cv代价与训练集个数m的关系

    :param X:
    :param y:
    :param Xval:
    :param yval:
    :param l:
    :return:
    """
    xx = range(1, X.shape[0] + 1)
    cv_cost, training_cost = [], []
    for i in xx:
        final_theta = trainLinerReg(X[:i], y[:i], l)
        cv_cost_i = costReg(final_theta, Xval, yval, 0)
        training_cost_i = costReg(final_theta, X[:i], y[:i], 0)
        cv_cost.append(cv_cost_i)
        training_cost.append(training_cost_i)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(xx, cv_cost, c='r', label='cv_cost')
    ax.plot(xx, training_cost, c='skyblue', label='training_cost')
    ax.legend()
    ax.set_xlabel('Number of training examples')
    ax.set_ylabel('Cost')
    ax.set_title('Learning curve for liner regression')
    plt.grid(True)
    plt.show()


def genPolyFeatures(X, power):
    Xploy = X.copy()
    for i in range(2, power + 1):
        Xploy = np.insert(Xploy, Xploy.shape[1], np.power(Xploy[:, 1], i), axis=1)
    return Xploy


def get_means_std(X):
    means = np.mean(X, axis=0)
    stds = np.std(X, axis=0, ddof=1)
    return means, stds


def featureNormalize(myX, means, stds):
    X_norm = myX.copy()
    X_norm[:, 1:] = X_norm[:, 1:] - means[1:]  # 对每个特征减去它的均值
    X_norm[:, 1:] = X_norm[:, 1:] / stds[1:]  # 再进行特征值缩放
    return X_norm


power = 6  # 扩展到x的6次方

train_means, train_stds = get_means_std(genPolyFeatures(X, power))
X_norm = featureNormalize(genPolyFeatures(X, power), train_means, train_stds)
Xval_norm = featureNormalize(genPolyFeatures(Xval, power), train_means, train_stds)
Xtest_norm = featureNormalize(genPolyFeatures(Xtest, power), train_means, train_stds)


def plot_fit(means, stds, l):
    """画出拟合曲线"""
    theta = trainLinerReg(X_norm, y, l)
    x = np.linspace(-75, 55, 50)
    xmat = x.reshape(-1, 1)
    xmat = np.insert(xmat, 0, 1, axis=1)
    Xmat = genPolyFeatures(xmat, power)
    Xmat_norm = featureNormalize(Xmat, means, stds)

    plot_data()
    plt.plot(x, Xmat_norm @ theta, 'b--')
    plt.show()


def select_lambda(X_norm, Xval_norm, y, yval):
    lambdas = [i for i in np.arange(0., 10., 0.2)]
    cv_cost, train_cost = [], []
    for l in lambdas:
        theta = trainLinerReg(X_norm, y, l)
        cv_cost.append(costReg(theta, X_norm, y, 0))
        train_cost.append(costReg(theta, Xval_norm, yval, 0))

    plt.figure(figsize=(8, 5))
    plt.plot(lambdas, cv_cost, label='Train')
    plt.plot(lambdas, train_cost, label='Cross Validation')
    plt.legend()
    plt.xlabel('lambda')
    plt.ylabel('Cost')
    plt.grid(True)
    plt.show()


select_lambda(X_norm, Xval_norm, y, yval)
