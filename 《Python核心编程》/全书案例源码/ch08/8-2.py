from multiprocessing import Process
import time


class NewProcess(Process):
    def run(self):                     	#重载run()函数
        while True:
            print("子进程")
            time.sleep(1)

if __name__ == '__main__':
    p = NewProcess()
    p.start()                           	#开启子进程

    while True:
        print("父进程")
        time.sleep(1)