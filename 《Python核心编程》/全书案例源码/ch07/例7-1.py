import re
print(re.match('I','I like Python').span())  #在起始位置匹配
print(re.match('world','hello world'))     #不在起始位置匹配