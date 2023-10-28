#定义函数
def describe_grade(name,grade='80'):
    '''显示学生的成绩信息'''
    print(name.title()+"'s score is "+grade+".")
#使用默认值的方式调用函数
describe_grade('adivol')
#调用函数，并为所有形参提供实参
describe_grade('Jack','100')