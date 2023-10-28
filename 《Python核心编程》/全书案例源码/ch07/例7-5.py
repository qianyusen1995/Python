import re
pattern = re.compile(r'\d+')   #查找数字
r1 = pattern.findall('1949年10月01日')
r2 = pattern.findall('2008年05月12日14时28分', 0, 10)
print(r1)
print(r2)
