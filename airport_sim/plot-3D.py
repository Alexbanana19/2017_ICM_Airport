# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:04:28 2017

@author: Alex
"""

import scipy.io as sio  
import matplotlib.pyplot as plt
import numpy as np

mat1 = 'C:\\Users\\Alex\\Desktop\\airport_sim\\delay.mat' 
data1 = sio.loadmat(mat1)

m = data1['delay2']
x = range(3,8)
hor = np.ones(5) * 1750

x1 = m[0]
y1 = m[1]
y2 = m[2]
y3 = m[3]
y4 = m[4]
y5 = m[5]
y6 = m[6]
y7 = m[7]
y8 = m[8]
ax=plt.subplot(1,3,1) #创建一个三维的绘图工程

#将数据点分成三部分画，在颜色上有区分度
ax.plot(x1, y1, c='y') #绘制数据点
ax.plot(x1, y2, c='orange')
ax.plot(x1, y3, c='r')
ax.plot(x1, y4, c = 'black')

ax.plot(x1, y5, c='purple') #绘制数据点
ax.plot(x1, y6, c='darkblue')
ax.plot(x1, y7, c='blue')
ax.plot(x1, y8, c = 'green')

ax.plot(x, hor, linestyle="--", c= 'grey')
ax.set_ylim(500, 3200)
ax.set_xticks([3,4,5,6,7])
plt.annotate('original',xy = (3,500), xytext=(3.2,1850))
plt.annotate('improved',xy = (3,500), xytext=(3.2,1600))
ax.set_ylabel('Mean Average Waiting Time') #坐标轴
ax.set_title('p = 0.2')

x1 = m[0]
y1 = m[9]
y2 = m[10]
y3 = m[11]
y4 = m[12]
y5 = m[13]
y6 = m[14]
y7 = m[15]
y8 = m[16]
ax=plt.subplot(1,3,2)

ax.plot(x1, y1, c='y') #绘制数据点
ax.plot(x1, y2, c='orange')
ax.plot(x1, y3, c='r')
ax.plot(x1, y4, c = 'black')

ax.plot(x1, y5, c='purple') #绘制数据点
ax.plot(x1, y6, c='darkblue')
ax.plot(x1, y7, c='blue')
ax.plot(x1, y8, c = 'green')

ax.plot(x, hor, linestyle="--", c= 'grey')
#ax.set_yticks([])
ax.set_xticks([3,4,5,6,7])
ax.set_ylim(500, 3200)
ax.set_yticks([])
plt.annotate('original',xy = (3,500), xytext=(3.2,1850))
plt.annotate('improved',xy = (3,500), xytext=(3.2,1600))
ax.set_xlabel('Passenger Delay')
ax.set_title('p = 0.4')

x1 = m[0]
y1 = m[17]
y2 = m[18]
y3 = m[19]
y4 = m[20]
y5 = m[21]
y6 = m[22]
y7 = m[23]
y8 = m[24]
ax=plt.subplot(1,3,3)

ax.plot(x1, y1, c='y') #绘制数据点
ax.plot(x1, y2, c='orange')
ax.plot(x1, y3, c='r')
ax.plot(x1, y4, c = 'black')

ax.plot(x1, y5, c='purple') #绘制数据点
ax.plot(x1, y6, c='darkblue')
ax.plot(x1, y7, c='blue')
ax.plot(x1, y8, c = 'green')

ax.plot(x, hor, linestyle="--", c= 'grey')
ax.set_yticks([])
plt.annotate('original',xy = (3,500), xytext=(3.2,1850))
plt.annotate('improved',xy = (3,500), xytext=(3.2,1600))
ax.set_xticks([3,4,5,6,7])
ax.set_ylim(500, 3200)
ax.set_title('p = 0.6')
plt.show()