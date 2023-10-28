from multiprocessing import Process
import time

def test(a):                             #要实现的子进程功能函数
    for i in range(a):
        print("子进程")
        time.sleep(1)

if __name__ == '__main__':
    p = Process(target=test, args=(5,))  	#实例化一个Process对象
    p.start()                            		#启动子进程
    p.join(1)
    while True:
        print("父进程")
        time.sleep(1)