import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat


def initCentroids(X, K):
    """
    从数据集中随机选取K个聚类中心

    :param X:
    :param K:
    :return:
    """
    m = X.shape[0]
    idx = np.random.choice(m, K)
    return X[idx]


def findCloset(X, centroids):
    """
    实现数据集的分类

    :param X:
    :param centroids:
    :return: 一维数组，表示数据点离第几个聚类中心最近
    """
    idx = []
    max_dis = 1_000_000
    for i in range(X.shape[0]):
        dis = X[i] - centroids
        all_distance = dis[:, 0] ** 2 + dis[:, 1] ** 2
        if all_distance.min() < max_dis:
            ci = np.argmin(all_distance)
            idx.append(ci)

    return np.array(idx)


def moveCentroids(idx, X):
    """
    实现聚类中心移动至该类的平均点

    :param idx:
    :param centroids:
    :param X:
    :return:
    """
    new_centroids = []
    for i in range(len(np.unique(idx))):
        new_centroid = X[i == idx].mean(axis=0)
        new_centroids.append(new_centroid)

    return np.array(new_centroids)


def plotData(X, idx, centroids):
    K = len(np.unique(idx))
    colors = ['b', 'g', 'gold', 'darkorange', 'salmon', 'olivedrab',
              'maroon', 'navy', 'sienna', 'tomato', 'lightgray', 'gainsboro',
              'coral', 'aliceblue', 'dimgray', 'mintcream',
              'mintcream']

    assert len(centroids[0]) <= len(colors), 'Colors out of index'

    subX = []
    for i in range(K):
        item = X[i == idx]
        subX.append(item)

    for i in range(K):
        xx = subX[i]
        plt.scatter(xx[:, 0], xx[:, 1], c=colors[i], label='Cluster %d'%i)
    plt.legend()
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Plot of X points')

    xx, yy = [], []
    for centroid in centroids:
        xx.append(centroid[:, 0])
        yy.append(centroid[:, 1])

    plt.plot(xx, yy, 'rx--')
    plt.show()


def runKmeans(X, centroids, times):
    K = len(centroids)
    all_centroids = [centroids]
    temp_centroids = centroids
    for i in range(times):
        idx = findCloset(X, temp_centroids)
        temp_centroids = moveCentroids(idx, X)
        all_centroids.append(temp_centroids)

    return all_centroids, idx


data = loadmat('ex7data2.mat')
X = data['X']
centroids = initCentroids(X, 3)
all_centroids, idx = runKmeans(X, centroids, 10)
plotData(X, idx, all_centroids)
