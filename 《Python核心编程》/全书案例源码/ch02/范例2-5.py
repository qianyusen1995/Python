num=int(input("输入一个数字："))
if num%2==0:
    if num%5==0:                              		#该行不允许并到上一行
       print ("你输入的数字可以整除 2 和 5")    		#该行允许并到上一行
    else:
       print ("你输入的数字可以整除 2，但不能整除5") 	#该行允许并到上一行
else:
    if num%5==0:                              		#该行不允许并到上一行
        print ("你输入的数字可以整除5，但不能整除 2")	#该行允许并到上一行
    else:
        print  ("你输入的数字不能整除 2 和 5")     	#该行允许并到上一行