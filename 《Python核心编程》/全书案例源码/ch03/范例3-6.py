score = eval(input("请输入您的考试成绩:"))
#获取用户考试成绩，并将值赋予变量score
if score >= 90:
#判断考试成绩是否大于或等于90分，如果是则执行下面的语句
    print("您的考试评级为：A级")
elif  90 > score >= 80:
#判断考试成绩是否大于或等于80分而小于90分，如果是则执行下面的语句
    print("您的考试评级为：B级")
elif  80 > score >= 70:
#判断考试成绩是否大于或等于70分而小于80分，如果是则执行下面的语句
    print("您的考试评级为：C级")
elif  70 > score >= 60:
#判断考试成绩是否大于或等于60分而小于70分，如果是则执行下面的语句
    print("您的考试评级为：D级")
else:
#如果上述条件判断均为假，则执行下面的语句
   print("您的考试评级为：不及格")
