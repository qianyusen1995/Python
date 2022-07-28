# coding=utf-8
# coding = UTF-8
# Python极简讲义 一本书入门数据分析与机器学习
# ! python3
myname = "jefferson qian"

# 列表,元组,字典，集合
list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 4, 3)
dict1 = {'a': 2, 'b': 2, 'c': 5}  # type: Dict[str, int]
human = {"man", "woman"}

# 遍历可迭代对象：list tuple set dict
for i in list1:
    print(i)
for i in dict1.keys():
    print(i)
for i in dict1.values():
    print([i])
pass
for key, value in [('a', 1), ('b', 2), ('c', 3)]:
    print({key: value})

# 数据的预处理
names = ['Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob']
print({name[0].upper() + name[1:].lower() for name in names if len(name) > 2})
# or print ({name.title() for name in names if len(name) > 2})
# 合并值，不区分键大小写一律小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {key.lower(): mcase.get(key.lower(), 0) + mcase.get(key.upper(), 0) for key in mcase.keys()}
print(mcase_frequency)

# "时间戳"
import time


def timeStamp(timeNum):
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)


a = 1629066062002  # 输入毫秒级的时间
timeStamp(a)  # 转出正常格式的时间
