x = 10                                #在函数体外定义全局变量x并为其赋值
y = 0                                 #在函数体外定义全局变量y并为其赋值
def fun():                           #定义函数
    global y              	#在函数体内使用关键字global定义全局变量
    y = 5                 	#给变量y赋值，在函数体内修改了全局变量y的值
    print('函数体内：全局变量x =',x)  	#在函数体内输出全局变量x的值
    print('函数体内：y =',y)          	#在函数体内输出全局变量y的值
fun()                              		#调用函数
print('函数体外：全局变量x =',x)     	#在函数体外输出全局变量x的值
print('函数体外：y =',y)             	#在函数体外输出全局变量y的值