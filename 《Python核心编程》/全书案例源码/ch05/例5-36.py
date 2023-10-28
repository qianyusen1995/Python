animal.discard('蟒蛇')
print("集合animal中的动物有：",animal)


animal.remove('蟒蛇')
Traceback (most recent call last):
  File "<input>", line 1, in <module>    #使用remove()函数，出现报错
KeyError: '蟒蛇'
