# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:04:28 2017

@author: Alex
"""

import scipy.io as sio  
import matplotlib.pyplot as plt
import numpy as np

mat1 = 'C:\\Users\\Alex\\Desktop\\airport_sim\\delay_var.mat' 
data1 = sio.loadmat(mat1)

m = data1['A']
x = range(3,8)
hor = np.ones(5) * 7000000

x1 = m[0]
y1 = m[1]
y2 = m[2]
y3 = m[3]
y4 = m[4]
y5 = m[5]
y6 = m[6]
y7 = m[7]
y8 = m[8]
bx=plt.subplot(1,3,1) #创建一个三维的绘图工程

#将数据点分成三部分画，在颜色上有区分度
bx.plot(x1, y1, c='y', marker='*') #绘制数据点
bx.plot(x1, y2, c='orange', marker='*')
bx.plot(x1, y3, c='r', marker='*')
bx.plot(x1, y4, c = 'black', marker='*')

bx.plot(x1, y5, c='purple', marker='*') #绘制数据点
bx.plot(x1, y6, c='darkblue', marker='*')
bx.plot(x1, y7, c='blue', marker='*')
bx.plot(x1, y8, c = 'green', marker='*')
plt.annotate('original',xy = (3,500), xytext=(3.2,0.75 * 10000000))
plt.annotate('improved',xy = (3,500), xytext=(3.2,0.62 * 10000000))
bx.plot(x, hor, linestyle="--", c= 'grey')
#bx.set_ylim(500, 3200)
bx.set_xticks([3,4,5,6,7])
bx.set_ylabel('Variance of Average Waiting Time') #坐标轴
bx.set_title('p = 0.2')

x1 = m[0]
y1 = m[9]
y2 = m[10]
y3 = m[11]
y4 = m[12]
y5 = m[13]
y6 = m[14]
y7 = m[15]
y8 = m[16]
bx=plt.subplot(1,3,2)

bx.plot(x1, y1, c='y', marker='*') #绘制数据点
bx.plot(x1, y2, c='orange',marker='*')
bx.plot(x1, y3, c='r',marker='*')
bx.plot(x1, y4, c = 'black',marker='*')

bx.plot(x1, y5, c='purple',marker='*') #绘制数据点
bx.plot(x1, y6, c='darkblue',marker='*')
bx.plot(x1, y7, c='blue',marker='*')
bx.plot(x1, y8, c = 'green',marker='*')

bx.plot(x, hor, linestyle="--", c= 'grey')
bx.set_xticks([3,4,5,6,7])
#bx.set_ylim(500, 3200)
plt.annotate('original',xy = (3,500), xytext=(3.2,0.75 * 10000000))
plt.annotate('improved',xy = (3,500), xytext=(3.2,0.62 * 10000000))
bx.set_xlabel('Passenger Delay')
bx.set_title('p = 0.4')

x1 = m[0]
y1 = m[17]
y2 = m[18]
y3 = m[19]
y4 = m[20]
y5 = m[21]
y6 = m[22]
y7 = m[23]
y8 = m[24]
bx=plt.subplot(1,3,3)

bx.plot(x1, y1, c='y', marker='*') #绘制数据点
bx.plot(x1, y2, c='orange', marker='*')
bx.plot(x1, y3, c='r', marker='*')
bx.plot(x1, y4, c = 'black', marker='*')

bx.plot(x1, y5, c='purple', marker='*') #绘制数据点
bx.plot(x1, y6, c='darkblue', marker='*')
bx.plot(x1, y7, c='blue', marker='*')
bx.plot(x1, y8, c = 'green', marker='*')
plt.annotate('original',xy = (3,500), xytext=(3.2,0.75 * 10000000))
plt.annotate('improved',xy = (3,500), xytext=(3.2,0.62 * 10000000))
bx.plot(x, hor, linestyle="--", c= 'grey')
bx.set_yticks([])
bx.set_xticks([3,4,5,6,7])
#bx.set_ylim(500, 3200)
bx.set_title('p = 0.6')
plt.show()