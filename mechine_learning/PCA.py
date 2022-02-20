import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

mat = loadmat('ex7data1.mat')
X = mat['X']
'''plt.scatter(X[:, 0], X[:, 1], facecolors='none', edgecolors='b')
plt.grid(True)
plt.show()'''


def featureNormalize(X):
    """
    在PCA之前需要标准化数据

    :param X: database
    :return: normalized X, means, std
    """
    means = X.mean(axis=0)

    # numpy在求标准差(方差)时，默认除以a.size，所以要声明ddof=1.而pandas的std函数无偏，要有偏就申明ddof=0
    std = X.std(axis=0, ddof=1)  # np.sqrt(((a - np.mean(a)) ** 2).sum() / (a.size - 1))

    X_norm = (X - means) / std
    return X_norm, means, std


def pca(X):
    U, S, V = np.linalg.svd(X)

    return U, S, V


X_norm, means, std = featureNormalize(X)
# print(X_norm.shape)
U, S, V = pca(X_norm)


# print(S.shape)


def projectData(X, V, K):
    """
    降维

    :param X:
    :param V:
    :param K:
    :return:
    """
    Z = X @ V[:, :K]

    return Z


def reconstructionData(Z, V, K):
    """
    压缩后的K维数据在原来的N维上看起来的样子。
    注意不能从K还原到N维了，参考二向箔

    :param Z:
    :param V:
    :param K:
    :return:
    """
    X_rec = Z @ V[:, :K].T

    return X_rec


def cost(S, K):
    return 1 - S[:K].sum() / S.sum()


Z = projectData(X_norm, V, K=1)
X_rec = reconstructionData(Z, V, K=1)

'''plt.figure(figsize=(7, 5))
plt.axis("equal")
plt.scatter(X_norm[:, 0], X_norm[:, 1], s=30, facecolors='none',
            edgecolors='b', label='Original Data Points')
plt.scatter(X_rec[:, 0], X_rec[:, 1], s=30, facecolors='none',
            edgecolors='r', label='PCA Reduced Data Points')

plt.title("Example Dataset: Reduced Dimension Points Shown", fontsize=14)
plt.xlabel('X1 [Feature Normalized]', fontsize=14)
plt.ylabel('X2 [Feature Normalized]', fontsize=14)
plt.grid(True)

for x in range(X_norm.shape[0]):
    plt.plot([X_norm[x, 0], X_rec[x, 0]], [X_norm[x, 1], X_rec[x, 1]], 'k--')
    # 输入第一项全是X坐标，第二项都是Y坐标
plt.legend()
plt.show()'''

'''print(Z)
数据集从二维压缩到一维后，在一维线上的位置
print("——————————————————————————")
print(X_rec)
压缩后的一维数据集从二维上看起来的样子
print("——————————————————————————")
print(X_norm)
未被压缩的数据集'''

mat1 = loadmat('ex7faces.mat')
X1 = mat1['X']


#  print(X1.shape)


def displayData(X, row=10, col=10):
    fig, axs = plt.subplots(row, col, figsize=(8, 8))
    for r in range(row):
        for c in range(col):
            axs[r][c].imshow(X[r * col + c].reshape(32, 32).T, cmap='Greys_r')
            axs[r][c].set_xticks([])
            axs[r][c].set_yticks([])
    plt.show()


X_norm1, means1, std1 = featureNormalize(X1)

U1, S1, V1 = pca(X_norm1)

Z1 = projectData(X_norm1, V1, K=100)
X_rec1 = reconstructionData(Z1, V1, K=100)
print(cost(S1, 100))
displayData(X_rec1, 5, 5)
