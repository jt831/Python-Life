import matplotlib.pyplot as plt
import random

# 使得matplotlib能够兼容中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 3月和4月的温度
y_3 = [random.randint(10, 23) for weather_3 in range(1, 32)]
y_4 = [random.randint(11, 25) for weather_4 in range(1, 31)]

# 天数
x_3 = range(1, 32)
x_4 = range(35, 65)

# 绘制散点图
plt.scatter(x_3, y_3, color="#FF7F50", label="3月温度")
plt.scatter(x_4, y_4, label="4月温度")

# 调整x轴
_x = list(x_3) + list(x_4)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["4月{}日".format(i - 34) for i in x_4]
plt.xticks(_x[::2], _xtick_labels[::2], rotation=45)

# 调整y轴
_y = range(11, 26)
plt.yticks(_y, rotation=45)
plt.ylabel("温度/C")

# 添加图例(结合plt.plot中的label，输出每种点表示什么, 以及图例在图形上的位置)
plt.legend(loc='upper left')

plt.title("3、4月温度图")

# 添加表格
plt.grid()
# 存储
# plt.savefig("./weather.svg")

plt.show()
