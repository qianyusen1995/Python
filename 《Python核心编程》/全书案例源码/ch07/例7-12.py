import re
m = re.match(r'(http://www|www)\.(.*)\..{3}','http://www.python.org')
m.group()	#输出匹配到的字符串

m.group(1)	#输出第一对圆括号中的内容

m.group(2)	#输出第二对圆括号中的内容

m.start(1)	#输出第一组子字符串的起始位置

m.start(2)	#输出第二组子字符串的起始位置

m.end(0)	#输出字符串的结束位置

m.span(1)	#输出第一组子字符串的起始和结束位置

