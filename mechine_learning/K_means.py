import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat


def findClosestCentroids(X, centroids):
    idx = []  # 一维数组，里面第i个值代表离第i个数据点最近的聚类中心的下标
    max_dist = 1_000_000  # 限制最大距离
    for i in range(len(X)):
        minus = X[i] - centroids  # 向量相减
        dist = minus[:, 0] ** 2 + minus[:, 1] ** 2  # 一维数组，表示第i个数据点离所有聚类中心距离的平方，本例中X为1*2向量
        if dist.min() < max_dist:  # 只是确保选出来的最小距离不要太大
            ci = np.argmin(dist)  # ci为离第i个数据点距离（的平方）最近的聚类中心的下标
            idx.append(ci)  # 存起来
    return np.array(idx)


mat = loadmat('ex7data2.mat')
X = mat['X']
init_centroids = np.array([[3, 3], [6, 2], [8, 5]])
idx = findClosestCentroids(X, init_centroids)


def computeCentroids(X, idx):
    centroids = []
    for i in range(len(np.unique(idx))):  # 聚类中心的个数
        u_k = X[idx == i].mean(axis=0)  # idx == i 得到一个[N * 1]的bool向量，选出那些属于第i个聚类中心的点，求均值
        centroids.append(u_k)  # 将均值作为新的聚类中心

    return np.array(centroids)


def plotData(X, centroids, idx=None):
    colors = ['b', 'g', 'gold', 'darkorange', 'salmon', 'olivedrab',
              'maroon', 'navy', 'sienna', 'tomato', 'lightgray', 'gainsboro',
              'coral', 'aliceblue', 'dimgray', 'mintcream',
              'mintcream']
    assert len(centroids[0]) <= len(colors), 'colors not enough'  # 断言聚类中心的个数小于颜色种类，否则报错

    subX = []
    if idx is not None:
        for i in range(len(centroids[0])):
            x_i = X[idx == i]
            subX.append(x_i)

    else:
        subX = [X]

    plt.figure(figsize=(8, 5))
    for i in range(len(subX)):
        xx = subX[i]
        plt.scatter(xx[:, 0], xx[:, 1], c=colors[i], label='Cluster %d' % i)
    plt.legend()
    plt.grid(True)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Plot of X Points')

    xx, yy = [], []
    for centroid in centroids:
        xx.append(centroid[:, 0])
        yy.append(centroid[:, 1])

    plt.plot(xx, yy, 'rx--')  # rx--表示画出聚类中心移动轨迹
    plt.show()


def runKmeans(X, centriods, run_times):
    K = len(centriods)

    centriods_all = [centriods]  # 记录从初始化到最终固定的所有的聚类中心
    centriod_i = centriods
    for i in range(run_times):
        idx = findClosestCentroids(X, centriod_i)
        centriod_i = computeCentroids(X, idx)
        centriods_all.append(centriod_i)

    return idx, centriods_all


def initCentroids(X, K):
    m = X.shape[0]
    idx = np.random.choice(m, K)

    return X[idx]


'''for i in range(3):
    init_centroids = initCentroids(X, 3)
    idx, centroids_all = runKmeans(X, init_centroids, 10)
    plotData(X, centroids_all, idx)'''
