a= zebra
b= bull
list = [lion,leopard,panda,tiger,wolf]
if ( a in list ):
    print (a "在指定列表list中")
else:
    print (a "不在指定列表list中")
if ( b not in list ):
    print (b "不在指定列表list中")
else:
    print (b "在指定列表list中")
a = panda      # 修改变量 a 的值为列表中存在的值
if ( a in list ):
    print (a "在指定列表中 list 中")
else:
    print (a "不在指定列表中 list 中")