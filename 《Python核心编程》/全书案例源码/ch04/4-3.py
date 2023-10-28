#定义函数
def parameter_test(para):
    print('原值：',para)
    para += para
#调用函数
print('=========值传递=========')
pa = 'Jack adivol'
print('函数调用前：',pa)
parameter_test(pa)              #实参为字符串，是不可变对象
print('函数调用后：',pa)
print('=========引用传递=========')
list = ['adivol','merry','jackson']
print('函数调用前：',list)
parameter_test(list)            #实参为列表，是可变对象
print('函数调用后：',list)