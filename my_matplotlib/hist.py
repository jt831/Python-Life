import matplotlib.pyplot as plt
import matplotlib.font_manager
import random

# 使得matplotlib能够兼容中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(20, 8), dpi=80)
# 给出初始数据
a = [random.randint(100, 150) for i in range(100, 151)]

dis = 2  # 组距


# 计算组数
def cal_num_bins(one_list):
    num_bins = (max(one_list) - min(one_list)) // dis
    return num_bins


plt.hist(a, cal_num_bins(a))  # 传入数据与要分成的组数,显示直方图

plt.xticks(range(min(a), max(a) + dis, dis))

plt.yticks(range(0, 40))
plt.ylabel("每个区间的组数")

plt.grid()

plt.show()
