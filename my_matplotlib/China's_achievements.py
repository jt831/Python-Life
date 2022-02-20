
# 绘制matplotlib折线图

import matplotlib.pyplot as plt
import random
# 使得matplotlib能够兼容中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置图形大小
plt.figure(figsize=(20, 10), dpi=80)

# 初始化x轴坐标
years1 = list(range(1980, 2011, 5))  # 只是以5为间隔显示数字，实际上还是输出了1980到2011的
years2 = list(range(2011, 2020))
years = years1 + years2

# 初始化y轴坐标
percentage = [random.randint(0, 101) for perc in range(0, 16)]

# 绘折线图
plt.plot(years, percentage)

# 调整x轴(这里啥也没干)
plt.xticks()

# 显示图像
plt.show()
