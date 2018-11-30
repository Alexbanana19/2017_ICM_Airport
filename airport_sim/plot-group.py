# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:04:28 2017

@author: Alex
"""

import scipy.io as sio  
import matplotlib.pyplot as plt
import numpy as np

mat1 = 'C:\\Users\\Alex\\Desktop\\airport_sim\\group.mat' 
data1 = sio.loadmat(mat1)

m = data1['group']
x = range(1,5)
hor = np.ones(4) * 1750

x1 = m[0]
y1 = m[1]
y2 = m[2]
y3 = m[3]
y4 = m[4]
y5 = m[5]
y6 = m[6]
ax=plt.subplot(1,3,1) #创建一个三维的绘图工程

#将数据点分成三部分画，在颜色上有区分度
ax.plot(x1, y1, c='y') #绘制数据点
ax.plot(x1, y2, c='orange')
ax.plot(x1, y3, c='r')


ax.plot(x1, y4, c='purple') #绘制数据点
ax.plot(x1, y5, c='darkblue')
ax.plot(x1, y6, c='blue')


ax.plot(x, hor, linestyle="--", c= 'grey')
ax.set_ylim(500, 3200)
ax.set_xticks([1,2,3,4])
plt.annotate('original',xy = (1,500), xytext=(1.2,1850))
plt.annotate('improved',xy = (1,500), xytext=(1.2,1600))
ax.set_ylabel('Mean of Average Waiting Time') #坐标轴
ax.set_title('p = 0.2')

x1 = m[0]
y1 = m[7]
y2 = m[8]
y3 = m[9]
y4 = m[10]
y5 = m[11]
y6 = m[12]

ax=plt.subplot(1,3,2)

ax.plot(x1, y1, c='y') #绘制数据点
ax.plot(x1, y2, c='orange')
ax.plot(x1, y3, c='r')


ax.plot(x1, y4, c='purple') #绘制数据点
ax.plot(x1, y5, c='darkblue')
ax.plot(x1, y6, c='blue')


ax.plot(x, hor, linestyle="--", c= 'grey')
ax.set_yticks([])
ax.set_xticks([1,2,3,4])
ax.set_ylim(500, 3200)
plt.annotate('original',xy = (1,500), xytext=(1.2,1850))
plt.annotate('improved',xy = (1,500), xytext=(1.2,1600))
ax.set_xlabel('Passengers Per Group')
ax.set_title('p = 0.4')

x1 = m[0]
y1 = m[13]
y2 = m[14]
y3 = m[15]
y4 = m[16]
y5 = m[17]
y6 = m[18]

ax=plt.subplot(1,3,3)

ax.plot(x1, y1, c='y') #绘制数据点
ax.plot(x1, y2, c='orange')
ax.plot(x1, y3, c='r')


ax.plot(x1, y4, c='purple') #绘制数据点
ax.plot(x1, y5, c='darkblue')
ax.plot(x1, y6, c='blue')
plt.annotate('original',xy = (1,500), xytext=(1.2,1850))
plt.annotate('improved',xy = (1,500), xytext=(1.2,1600))

ax.plot(x, hor, linestyle="--", c= 'grey')
ax.set_yticks([])
ax.set_xticks([1,2,3,4])
ax.set_ylim(500, 3200)
ax.set_title('p = 0.6')
plt.show()