import threading
def printf(str,num):
    for i in range(num):
        print('同学%d说：%s'%(i+1,str[i]))

if __name__=='__main__':
    s = ['我是小明', '我是小红', '我是小芳', '我是小刚','我是小华']
#threading.Thread()函数直接返回一个对象p
t=threading.Thread(target=printf,args=(s,5))
    t.start()    #对象p调用start()函数