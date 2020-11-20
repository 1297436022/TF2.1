import tensorflow as tf


# 从均匀分布中输出随机值,生成的值在该 [minval, maxval) 范围内遵循均匀分布
f = tf.random.uniform([2, 2], minval=0, maxval=1)
print("f:", f)
