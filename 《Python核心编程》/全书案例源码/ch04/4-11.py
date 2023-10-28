def recur_fac(n):             	#定义递归函数来计算正整数n的阶乘
    if n == 1:               		#当n为1时结束递归
        return 1
    return n * recur_fac(n-1)  	#进行函数递归

print('4的阶乘:',recur_fac(4))  	#打印4的阶乘结果