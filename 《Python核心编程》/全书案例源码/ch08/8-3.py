import _thread
from time import sleep, ctime    #显示时间
def thread1():
    print('线程1开始：', ctime())
    print('线程1挂起4秒')
    sleep(4)
    print('线程1结束：', ctime())
def thread2():
    print('线程2开始：', ctime())
    print('线程2挂起2秒')
    sleep(2)
    print('线程2结束：', ctime())
def thread3():
    print('线程3开始：', ctime())
    print('线程3挂起1秒')
    sleep(1)
    print('线程3结束',ctime())
def main():
    print('主线程开始!')
    #线程函数为无参数函数，args为空元组
    _thread.start_new_thread(thread1, ())  
    _thread.start_new_thread(thread2, ())
    _thread.start_new_thread(thread3, ())
    sleep(6)    #主线程睡眠，等待子线程结束
    print('全部结束:', ctime())
if __name__ == '__main__':
    main()