import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat
from sklearn import svm

mat = loadmat('ex6data1.mat')
X = mat['X']
y = mat['y']


def plotData(X, y):
    plt.figure(figsize=(8, 5))
    plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), cmap='rainbow')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.grid(True)
    plt.show()


def plotBoundary(clf, X):
    x_min, x_max = X[:, 0].min() * 1.2, X[:, 0].max() * 1.1
