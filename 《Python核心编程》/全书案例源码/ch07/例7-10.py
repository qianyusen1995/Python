import re
text='My name is Python'
re.sub('Python','MySQL',text)#用“MySQL”替换“Python”

re.sub('is|Python','cat',text)#用“cat”替换“is”或“Python”

re.subn('is|Python','dog',text,1)#用“dog”替换“is”或“Python”，只替换一次

r=re.subn('is|Python','pig',text)#用“pig”替换“is”或“Python”
print(r[0])#输出元组的第一项

print(r[1])#输出元组的第二项

