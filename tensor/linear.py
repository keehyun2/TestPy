# 노동시간 / 하루매출 
# 노동시간으로 하루 매출 예측
import tensorflow
tf = tensorflow.compat.v1

xData = [1,2,3,4,5,6,7] # 노동시간 
yData = [25000, 55000, 75000, 110000, 128000, 155000, 180000] # 하루매출
W = tf.Variable(tf.random_uniform([1] , -100, 100)) # 가중치
b = tf.Variable(tf.random_uniform([1] , -100, 100)) 

X=tf.placeholder(tf.float32)
Y=tf.placeholder(tf.float32)

H = W * X + b
cost = tf.reduce_mean(tf.square(H - Y))
# 경사하강
a= tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
for i in range(5001):
    sess.run(train, feed_dict={X: xData, Y: yData})
    if i % 500 == 0:
        print (i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))
print (sess.run(H, feed_dict={X: [9]})) # 9시간 일했을때 매출