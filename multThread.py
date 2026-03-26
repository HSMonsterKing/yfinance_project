#多核心示範 同一時間執行兩個以上的任務

from concurrent.futures import ThreadPoolExecutor
import time

def JobA():
    for i in range(100):
        print("這是 JobA....")
        time.sleep(1) # 暫停一秒

def JobB():
    for i in range(100):
        print("這是另一種 JobB....")
        time.sleep(1) # 暫停一秒

def JobC():
    for i in range(100):
        print("這是任務 JobC....CC")
        time.sleep(1) # 暫停一秒

def JobD():
    for i in range(100):
        print("這是任務 JobD.... DDDDDDD")
        time.sleep(1) # 暫停一秒

# 沒有 多執行緒的狀態下
# JobA()
# JobB()
# JobC()
# JobD()

# 多工版本

with ThreadPoolExecutor() as ex:
    ex.submit(JobA)
    ex.submit(JobB)
    ex.submit(JobC)
    ex.submit(JobD)