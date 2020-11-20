import tensorflow as tf

# normal 从服从指定正态分布的序列中随机取出指定个数的值
d = tf.random.normal([2, 2], mean=0.5, stddev=1)
print("d:", d)
# truncated_normal 截断的产生正态分布的随机数，即随机数与均值的差值若大于两倍的标准差，则重新生成
e = tf.random.truncated_normal([2, 2], mean=0.5, stddev=1)
print("e:", e)
