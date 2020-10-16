# @Time     :2020/10/15  18:35
# @Author   :wang-kai
# @tel      :15313929271
# @File    :线程作业.py

"""
1.用一个队列来存放商品
2.创建一个生产商品线程类,当商品数量小于50,开始生产,每次200个商品,每生产完一轮暂停一秒
3.创建五个消费商品线程类,当商品大于10时,开始消费,循环消费,每次消费3个,但商品数量小于10,暂停2秒
"""
from queue import Queue
from threading import Thread
import time

#创建一个队列,存储商品
q = Queue()
# 生产者线程
class producer(Thread):
    def run(self):
        # 判断数量是否小于50，小于50就生产200个
        count = 0
        while True:
            if q.qsize()<50:
                count += 1
                goods = '---第{}个商品---'.format(count)
                q.put(goods)
                print('生产', goods)
            time.sleep(1)

p = producer()
p.start()