import numpy as np
import tensorflow as tf

# 生成等间隔数值点 [a, b, c]  区间[a,b), c表示间隔
x, y = np.mgrid[1:3:1, 2:4:0.5]
# ravel() 将x, y拉直, np.c_ 并合并配对为二维张量，生成二维坐标点
grid = np.c_[x.ravel(), y.ravel()]
print("x:\n", x)
print("y:\n", y)
print("x.ravel():\n", x.ravel())
print("y.ravel():\n", y.ravel())
print('grid:\n', grid)


