import matplotlib.pyplot as plt

import random

list1 = [0, 1, 2, 3]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(20, 8), dpi=80)

x = range(11, 31)


y = [random.sample(list1, 1) for i in range(20)]

plt.plot(x, y)

x_list = [year for year in range(11, 31)]
plt.xticks(x_list, rotation=45)
plt.xlabel("年龄/year")

y_list = list1
plt.yticks(y_list, rotation=45)
plt.ylabel("老婆个数/人")

plt.title("舰长每年老婆的个数")

plt.savefig("./wife_size.svg")
plt.show()
