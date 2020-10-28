import matplotlib.pyplot as plt
import numpy as np
# 解决中文乱码
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# 生成数据
x = np.linspace(0.5, 7.5, 1000)
y = np.sin(x)
# pyplot模块中的figure()函数创建名为fig的Figure对象
fig = plt.figure(figsize=(12, 8))
# 在Figure对象中创建一个Axes对象，每个Axes对象即为一个绘图区域
ax = fig.add_subplot(111)
# sin(x)图
ax.plot(x, y, '--g', lw=2, label='sin(x)')

# 调整坐标轴范围
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
# 设置坐标轴标签
ax.set_xticks(np.arange(0, 10, 2))
ax.set_yticks(np.arange(-1, 1.5, 1))
ax.set_xticklabels(['2015-07-02', '2015-08-02', '2015-09-02', '2015-10-02', '2015-11-02'], \
                   rotation=45, fontsize=15)
ax.set_yticklabels([u'最小值', u'零值', u'最大值'], fontsize=15)

# 设置轴标签
ax.set_xlabel('X axis', fontsize=15)
ax.set_ylabel('Y axis', fontsize=15)
# 设置网格线
ax.grid(True, ls=':', color='r', alpha=0.5)
# 设置标题
ax.set_title(u"Functional Programming", fontsize=25)
# 添加图例
ax.legend(loc='upper right', fontsize=15)

# 添加sin(x)的最高点注释
ax.annotate('max sell',
            xy=(np.pi / 2, 1),  # 箭头指向点的坐标
            xytext=(np.pi / 2, 1.3),  # 注释文本左端的坐标
            weight='regular',  # 注释文本的字体粗细风格，bold是粗体，regular是正常粗细
            color='g',  # 注释文本的颜色
            fontsize=15,  # 注释文本的字体大小
            arrowprops={
                'arrowstyle': '->',  # 箭头类型
                'connectionstyle': 'arc3',  # 连接类型
                'color': 'g'  # 箭头颜色
            })

# 添加sin(x)的最低点注释
ax.annotate('min buy',
            xy=(np.pi * 3 / 2, -1),
            xytext=(np.pi * 3 / 2, -1.3),
            weight='regular',
            color='r',
            fontsize=15,
            arrowprops={
                'arrowstyle': '->',
                'connectionstyle': 'arc3',
                'color': 'r'
            })
# 显示图形
plt.show()
