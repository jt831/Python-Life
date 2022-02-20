import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from K_means import initCentroids, runKmeans

# 我们将把图片压缩成16中颜色
A = io.imread('bird_small.png')
A = A/225  # A[N * 3] is the value of RGB, divide by 255 so all values are in the range 0~1
X = A.reshape(-1, 3)  # reshape the image into an (N, 3) matrix
K = 16
centriods = initCentroids(X, K)
idx, centroids_all = runKmeans(X, centriods, 10)

img = np.zeros(X.shape)  # create an blank img
centriod = centroids_all[-1]

for i in range(len(centriod)):
    img[i == idx] = centriod[i]

img = img.reshape((128, 128, 3))  # 改回原始图片A的shape

fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].imshow(A)
axs[1].imshow(img)
plt.show()
