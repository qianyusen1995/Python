import threading
from time import sleep, ctime

class MyThread(threading.Thread):	#定义一个继承threadingthreading.Thread的类
    def __init__(self,num):   		#重载__init__()函数
        super().__init__()   			#调用父类的__init__()函数
        self.num=num;
    
def run(self):   #重载threading.Thread类中的run()函数
        sleep(2)
        print('同学%d说：现在是：'%(self.num),ctime())

if __name__ == "__main__":
    a = MyThread(2)    	#创建MyThread类的两个实例
    b = MyThread(3)
    a.start()            	#启动线程
    b.start()