import tensorflow as tf

x = tf.Variable(4.0)
with tf.GradientTape() as tape:
    y = x**3 + 2 * x + 1
grad = tape.gradient(y, x)
print(grad)
