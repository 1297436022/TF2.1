import numpy as np

# np.random.RandomState 伪随机数生成器 伪随机数是用确定性的算法计算出来的似来自[0,1]均匀分布的随机数序列
rdm = np.random.RandomState(seed=1)
a = rdm.rand()
b = rdm.rand(2, 3)
print("a:", a)
print("b:", b)
