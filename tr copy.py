import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# 初始化图形
fig, ax = plt.subplots()
bars = ax.bar([], [])
ax.set_ylim(0, 100)
ax.set_title('Real-time Bar Chart')
ax.set_xlabel('Category')
ax.set_ylabel('Value')

# 更新柱状图的函数
def update_bar_chart(frame):
    # 这里假设你有一个获取数据的函数或者实时数据源
    # 在这个示例中，我们随机生成一个包含5个随机值的列表
    data = [random.randint(0, 100) for _ in range(5)]

    # 清空现有的柱状图
    ax.clear()

    # 绘制新的柱状图
    bars = ax.bar(range(len(data)), data)

    # 设置图形属性
    ax.set_ylim(0, max(data) + 10)
    ax.set_title('Real-time Bar Chart')
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')

    return bars

# 创建动画
ani = FuncAnimation(fig, update_bar_chart, frames=range(10), interval=1000, repeat=False)

# 显示图形
plt.show()




