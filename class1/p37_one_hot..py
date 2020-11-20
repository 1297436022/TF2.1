import tensorflow as tf

classes = 3
labels = tf.constant([1, 0, 2])  # 输入的元素值最小为0，最大为2

# 独热编码，在分类问题中，常用独热码做标签
output = tf.one_hot(labels, depth=classes)  # 独热码 0:1 0 0  1:0 1 0  2:0 0 1
print("result of labels1:", output)
print("\n")
