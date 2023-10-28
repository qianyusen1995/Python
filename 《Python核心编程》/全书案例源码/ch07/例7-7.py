import re
str1='I like Python'
re.split(' ',str1)		#使用空格分隔字符串，注意引号中间有空格

s=re.split(' ',str1,1)	#只分隔一次
for i in s:				#遍历分隔后的字符串列表
    print(i)

re.split('i',str1)		#使用“i”作为分隔符

