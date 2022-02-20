import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

path = "ex2data2.txt"
data2 = pd.read_csv(path, header=None, names=['Test1', 'Test2', 'Accepted'])


def plot_data():
    """
    To show the primitive data

    :return:
    """
    positive = data2[data2['Accepted'].isin([1])]  # 这种['Accepted]方式与regression1的访问方式都可以
    negative = data2[data2['Accepted'].isin([0])]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(positive['Test1'], positive['Test2'], c='red', s=50, marker='o', label='Accepted')
    ax.scatter(negative['Test1'], negative['Test2'], c='blue', s=50, marker='x', label='Rejected')
    ax.legend(loc='center left', bbox_to_anchor=(0.25, 1.11), ncol=2)
    ax.set_xlabel('Test1 Score')
    ax.set_ylabel('Test2 Score')
    plt.show()


def feature_mapping(x1, x2, power):
    """
    特征值映射，用于扩大特征值
    
    :param x1:
    :param x2:
    :param power:
    :return:
    """
    data = {}
    for i in np.arange(power + 1):
        for p in np.arange(i + 2):  # 对于此数据集来说 i + 2 比 i + 1的准确率高
            data["f{}{}".format(i, p)] = np.power(x1, i - p) * np.power(x2, p)

    return pd.DataFrame(data)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost_fun(theta, X, Y):  # 一个细节：如果要运用高级优化而不是梯度下降，theta这个参数要放在第一个
    """
    不带正则化的代价函数J

    :param theta:
    :param X:
    :param Y:
    :return:
    """
    first = (-Y) * np.log(sigmoid(X.dot(theta.T)))
    second = (1 - Y) * np.log(1 - sigmoid(X.dot(theta.T)))
    cost = np.mean(first - second)  # 这里只能是mean而不能除以X.shape[0]，前者的结果是一个数，后者是一个【lines * 1】的矩阵

    return cost


def costReg(theta, X, Y, l=1):
    """
    正则化的代价函数J，即在普通的代价函数后面 + 很大的数乘以theta（惩罚项reg），通过“惩罚”来降低theta值

    :param theta:
    :param X:
    :param Y:
    :param l: 正则化参数λ，因为λ不在ASCII码里所以用首字母l替代（lambda）
    :return:
    """
    _theta = theta[1:]  # 一般不 “惩罚” θ0（x0）
    reg = (l / (2 * X.shape[0])) * (_theta.dot(_theta))

    return cost_fun(theta, X, Y) + reg


def gradient(theta, X, Y):
    """
    单纯计算偏倒数（梯度）

    :param theta:
    :param X:
    :param Y:
    :return:
    """
    return (X.T.dot((sigmoid(X.dot(theta.T)) - Y))) / X.shape[0]


def gradientReg(theta, X, Y, l=1):
    reg = (l / X.shape[0]) * theta
    reg[0] = 0
    return gradient(theta, X, Y) + reg


def predict(X, theta):
    """
    预测函数。根据训练好的θ和现有成绩X预测学生是否能被录取

    :param X:
    :param theta:
    :return:
    """
    prob = sigmoid(X.dot(theta.T))
    return [1 if x >= 0.5 else 0 for x in prob]


x1 = data2['Test1'].values
x2 = data2['Test2'].values
_data2 = feature_mapping(x1, x2, power=6)

print(_data2.head())
"""注意，这里没有添加X0，因为特征映射时已经添加了.
所以_data2的行数（即数据输入量）仍为m，列数（即特征数）扩大了但只包括x0到xn，不含y
"""
X = np.array(_data2)
Y = np.array(data2['Accepted'])
theta = np.zeros(X.shape[1])

cols = _data2.shape[1]
lines = _data2.shape[0]

assert(X.shape == (lines, cols))
assert(Y.shape == (lines, ))  # 逻辑回归中的Y和θ都要变成这种很怪的一维向量，不然会报错
assert(theta.shape == (cols, ))

#  print(gradientReg(theta, X, Y, 1))


result = opt.fmin_tnc(func=costReg, x0=theta, fprime=gradientReg, args=(X, Y, 2))

final_theta = result[0]
prediction = predict(X, final_theta)
correct = [1 if y_hat == y else 0 for (y_hat, y) in zip(prediction, Y)]
accuracy = np.mean(correct)
print(accuracy)
