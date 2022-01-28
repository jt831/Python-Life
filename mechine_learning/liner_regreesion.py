
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = 'ex1data1.txt'
# names添加列名，header用指定的行来作为标题，若原无标题且指定标题则设为None
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])

"""
打印出数据集的前五行
print(data.head())

绘制数据集的散点图
data.plot(kind='scatter', x='Population', y='Profit', figsize=(8, 5))
plt.show()
"""
data.insert(0, 'Ones', 1)  # 将名为‘Ones’的数据为1的列插入到第0列。目的是将θ0视为x0

cols = data.shape[1]  # 返回data的列数，现在是n + 2列。即x0到xn一共n+1列 + y的那1列
lines = data.shape[0]  # 返回data的行数，即m行

# 构造[m * (n + 1)]的输入矩阵X。第一个逗号前表示访问所有行，后表示从第0列到第n - 1列
X = data.iloc[:, 0:cols - 1]

# 构造[m * 1]输出值矩阵Y
y = data.iloc[:, cols - 1:cols]

# 将pandas格式装换为numpy格式
X = np.array(X.values)
y = np.array(y.values)

theta = np.zeros((1, cols - 1))  # 将θ初始化成全为0的[1, n + 1]矩阵

# 使用断言确保我的格式是对的
assert (X.shape == (lines, cols - 1))
assert (y.shape == (lines, 1))
assert (theta.shape == (1, cols - 1))


def computeCost(X, Y, theta):
    """

    :param X: 数据集输入值构成的[m * (n + 1)]矩阵
    :param Y: 数据集输出值构成的[m * 1]矩阵
    :param theta: 参数矩阵θ，一个[1 * (n + 1)]矩阵
    :return: 代价函数J(θ)
    """
    m = X.shape[0]  # m是数据集的大小
    inner = np.power((X.dot(theta.T) - Y), 2)
    cost = np.sum(inner) / (2 * m)
    return cost


def gradientDescent(X, y, theta, learning_rate=0.01, times=1000):
    m = X.shape[0]
    cost = np.zeros(times)
    #  不用担心拟合次数过多的问题，随着次数的增加斜率会越来越趋近于0，所以多拟合只是浪费一点计算时间而已
    for i in range(times):
        theta -= (learning_rate / m) * ((X.dot(theta.T) - y).T.dot(X))
        cost[i] = computeCost(X, y, theta)
    return theta, cost


final_theta, cost = gradientDescent(X, y, theta, 0.01)


x = np.linspace(data.Population.min(), data.Population.max(), 100)  # 横坐标
f = final_theta[0, 0] + (final_theta[0, 1] * x)  # 纵坐标，利润

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, f, color="red", label='Prediction')  # 绘制折线图
ax.scatter(data['Population'], data.Profit, label='Training Data')  # 绘制散点图
ax.legend(loc="upper left")  # 设置图标。顺便说一句，没有这句，上面那些label设置了也没用
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()


fig1, ax = plt.subplots(figsize=(8, 4))
ax.plot(np.arange(1000), cost, color='red')  # np.arange()返回等差数组
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()
