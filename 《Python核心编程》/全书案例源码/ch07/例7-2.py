import re
line = "Dogs are people's friend"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())#输出整个字符串
   print ("matchObj.group(1) : ", matchObj.group(1))#输出第一组字符串
   print ("matchObj.group(2) : ", matchObj.group(2))#输出第二组字符串
else:
   print ("No match")