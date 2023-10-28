#定义递归函数，获取斐波那契数列中第n个数字的值
def fibonacci_seq(n):  
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_seq(n-1)+fibonacci_seq(n-2)
#把获取到的斐波那契数字存放到列表中
nums=[ ]
for i in range(1,11):
#先使用fibonacci_seq()函数获得一个斐波那契数字，然后使用append()函数将其添加到列表中
nums.append(fibonacci_seq(i)) 
#打印斐波那契数列
print(nums)