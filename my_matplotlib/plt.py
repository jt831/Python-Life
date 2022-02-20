import random

import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(25, 8), dpi=80)

x = range(0, 120)

y = [random.randint(20, 35) for i in range(120)]

plt.plot(x, y)  # 传入x和y, plot将它们一一对应

x_list = list(x)

_xtick_labels = []

j = 1
while j <= 12:
    _xtick_labels += ["{}.{}".format(j, k) for k in range(60)]
    j += 1

plt.xticks(x_list[::5], _xtick_labels[::30], rotation=45)  # 调整x轴的刻度，角度
plt.xlabel("时间/t", rotation=45)

plt.yticks(rotation=45)
plt.ylabel("温度/C")

plt.title("一天中每半个小时气温变化情况")
# 保存
plt.savefig("./sig_size.svg")
plt.show()
