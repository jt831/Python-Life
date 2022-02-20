import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

"""
数据集包含学生两门考试的结果（输入x）以及该生是否进入了大学（输出y）
"""
path = "ex2data1.txt"
data = pd.read_csv(path, header=None, names=['exam1', 'exam2', 'admitted'])

#  基于对“admitted”列的bool索引返回的bool值对整个DataFrame过滤
positive = data[data.admitted.isin([1])]  # 筛选‘admitted’值为1的行列
negative = data[data.admitted.isin([0])]  # 筛选‘admitted’值为0的行列

fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(positive['exam1'], positive['exam2'], color='blue', label='Admitted')
ax.scatter(negative['exam1'], negative['exam2'], color='red', marker='x', label='Not Admitted')
# 设置图例显示在图的上方
'''这段没啥大用
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])'''
ax.legend(loc='center left', bbox_to_anchor=(0.2, 1.12), ncol=3)

# 设置横纵坐标名
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')
plt.show()


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost_fun(theta, X, Y):  # 一个细节：如果要运用高级优化而不是梯度下降，theta这个参数要放在第一个
    first = (-Y) * np.log(sigmoid(X.dot(theta.T)))
    second = (1 - Y) * np.log(1 - sigmoid(X.dot(theta.T)))
    cost = np.mean(first - second)  # 这里只能是mean而不能除以X.shape[0]，前者的结果是一个数，后者是一个【lines * 1】的矩阵

    return cost


def gradiant(theta, X, Y):
    """
    单纯计算偏倒数（梯度）

    :param theta:
    :param X:
    :param Y:
    :return:
    """
    return (X.T.dot((sigmoid(X.dot(theta.T)) - Y))) / X.shape[0]


def predict(X, theta):
    """
    预测函数。根据训练好的θ和现有成绩X预测学生是否能被录取

    :param X:
    :param theta:
    :return:
    """
    prob = sigmoid(X.dot(theta.T))
    return [1 if x >= 0.5 else 0 for x in prob]


data.insert(0, 'Ones', 1)  # 插入x0
#  获取行列
lines = data.shape[0]
cols = data.shape[1]
# 构造数据集
X = data.iloc[:, 0: cols - 1]
Y = data.iloc[:, -1]  # 注意这里的shape是（lines，）而不是(lines, 1)
theta = np.zeros(X.shape[1])  # 这里是(cols - 1, )而不是(1, cols - 1)


X = np.array(X)
Y = np.array(Y)

assert (X.shape == (lines, cols - 1))
assert (Y.shape == (lines, ))
assert (theta.shape == (cols - 1, ))

#  通过高级优化算法而非梯度下降得到θ
result = opt.fmin_tnc(func=cost_fun, x0=theta, fprime=gradiant, args=(X, Y))

final_theta = result[0]  # 取得训练后的θ
predictions = predict(final_theta, X)  # 取得预测结果
correct = [1 if a == b else 0 for (a, b) in zip(predictions, Y)]  # 将预测结果和真实结果对比
accuracy = np.mean(correct)  # 查看准确性
print(accuracy)

# 绘制决策边界
x1 = np.arange(130, step=0.1)
x2 = -(final_theta[0] + x1 * final_theta[1]) / final_theta[2]

fig1, ax = plt.subplots(figsize=(8, 5))
ax.scatter(positive['exam1'], positive['exam2'], c='b', label='Admitted')
ax.scatter(negative['exam1'], negative['exam2'], c='r', marker='x', label='Not Admitted')
ax.plot(x1, x2, c='skyblue')
ax.legend(loc='upper left')
ax.set_xlim(0, 130)
ax.set_ylim(0, 130)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Decision Boundary')
plt.show()

