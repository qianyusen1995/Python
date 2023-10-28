import re
print(re.search('I','I like Python').span())  		#在起始位置匹配
print(re.search('world','hello world').span())   	#不在起始位置匹配
