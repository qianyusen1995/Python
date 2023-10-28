import re
line = "Dogs are people's friend"
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print ("searchObj.group() : ", searchObj.group())  #输出整个字符串
   print ("searchObj.group(1) : ", searchObj.group(1))#输出第一组字符串
   print ("searchObj.group(2) : ", searchObj.group(2))#输出第二组字符串
else:
   print ("Nothing found")
