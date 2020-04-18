import csv
import pydash

with open('data.csv', 'rt', encoding='UTF8') as csvfile:
    next(csvfile, None) # 첫째줄 건너뛰기
    data = list(csv.reader(csvfile))

# dtArr = pydash.collections.map_(data, 0) # 날짜
priceArr = pydash.collections.map_(data, 1) # 시가
# dt = pydash.collections.map_(dtArr, lambda a: int(a.replace("/","")) )
price = pydash.collections.map_(priceArr, lambda a: int(a.replace(",","")) )

price = price[0:15] # 배열 갯수가 많아지면 에러 나는듯

print(price)
a = []

for idx in range(len(price)):
    a.append(idx + 1)

# print(dt[0])
print(price[0])

import tensorflow
tf = tensorflow.compat.v1

xData = a # 노동시간 
yData = price # 하루매출
print(xData)
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
init = tf.global_variables_initializer() # 변수 담은 값을 

sess = tf.Session()
sess.run(init)
for i in range(5001):
    sess.run(train, feed_dict={X: xData, Y: yData})
    # if i % 500 == 0:
    #     print (i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))
print (sess.run(H, feed_dict={X: [8]})) # 9시간 일했을때 매출
