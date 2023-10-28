num=int(input("输入一个数字："))
if num%2==0:
    if num%5==0:                                 #单层代码缩进
       print ("你输入的数字可以整除 2 和 5")     #多层代码缩进（缩进嵌套）
    else:
       print ("你输入的数字可以整除 2，但不能整除5")
else:
    if num%5==0:
        print ("你输入的数字可以整除5，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 5")