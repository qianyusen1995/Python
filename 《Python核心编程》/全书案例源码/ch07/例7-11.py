import re
m=re.match(r'^(\d+)-(\d+)$','010-123456')
print(m.group(0))#输出匹配到的字符串
print(m.group(1))#输出第一组字符串
print(m.group(2))#输出第二组字符串
