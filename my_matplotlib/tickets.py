import matplotlib.pyplot as plt
import random

# 使得matplotlib能够兼容中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(20, 8), dpi=80)

movie_name = ["战狼2", "蜘蛛侠", "敦刻尔克"]

# y轴
ticks_1 = [2000, 9000, 5000]
ticks_2 = [5000, 850, 6000]
ticks_3 = [8000, 800, 6000]
ticks_4 = [9000, 8400, 6500]

# x轴
x_14 = range(len(movie_name))
x_15 = [i + 0.1 for i in x_14]
x_16 = [i + 0.1 for i in x_15]
x_17 = [i + 0.1 for i in x_16]


plt.bar(x_14, ticks_1, width=0.1, label="Day01")
plt.bar(x_15, ticks_2, width=0.1, label="Day02")
plt.bar(x_16, ticks_3, width=0.1, label="Day03")
plt.bar(x_17, ticks_4, width=0.1, label="Day04")


_x = [i + 0.05 for i in x_15]
plt.xticks(_x, movie_name)

plt.legend(loc="upper right")
plt.show()
