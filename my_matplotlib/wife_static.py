import matplotlib.pyplot as plt

import random


# 使得matplotlib能够兼容中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置图形大小
fig = plt.figure(figsize=(20, 8), dpi=70)

# 添加水印
plt.text(x=20, y=1.5, rotation=45,
         ha='center',
         va='bottom',
         fontsize=50,  # 调整字体大小
         s='玖途', alpha=0.4, color='red')

# 初始化x轴
x = range(11, 31)

# 初始化y轴
wife_num = [0, 1, 2, 3]
y1 = [random.sample(wife_num, 1) for i in range(20)]
y2 = [random.sample(wife_num, 1) for j in range(20)]

# 绘折线图
plt.plot(x, y1, label="舰长1号", linewidth='3')
plt.plot(x, y2, label="舰长2号", color="#FF7F50", linestyle='--')

# 设置x轴刻度
x_list = [year for year in range(11, 31)]
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x_list, _xtick_labels, rotation=45)
plt.xlabel("年龄/year")

# 设置y轴刻度
y_list = wife_num
plt.yticks(y_list, rotation=45)
plt.ylabel("老婆个数/人")

# 设置表格题目
plt.title("舰长每年新老婆的个数")

# 绘制网格
plt.grid(color="#B766AD")

# 添加图例(结合plt.plot中的label，输出每条线表示什么, 以及图例在图形上的位置)
plt.legend(loc='upper right')

# 存储图表
# plt.savefig("./wife_size.svg")

# 显示图表
plt.show()
