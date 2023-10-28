import re
s='girl fr   ien  d'
print(re.sub(r' +','',s))	#将字符串中的空格替换成空字符串
print(re.subn(r' +','',s))	#将字符串中的空格替换成空字符串，并返回替换次数
