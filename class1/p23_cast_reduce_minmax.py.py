import tensorflow as tf

x1 = tf.constant([1., 2., 3.], dtype=tf.float64)
print("x1:", x1)

# tf.cast 类型转换
x2 = tf.cast(x1, tf.int32)
print("x2", x2)
# tf.reduce_min 用来计算一个张量的各个维度上元素的最小值
print("minimum of x2：", tf.reduce_min(x2))
print("maxmum of x2:", tf.reduce_max(x2))
