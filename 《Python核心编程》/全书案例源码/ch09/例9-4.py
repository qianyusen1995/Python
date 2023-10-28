import xml.etree.ElementTree as ET
          #读取待修改文件
updateTree = ET.parse("04.xml")
root = updateTree.getroot()
#创建新节点并添加为root的子节点
newEle = ET.Element("wangwu")
newEle.attrib = {"xuehao":"201809","age":"20"}
newEle.text = "这是一个新同学"
root.append(newEle)

#修改sub1的name属性
sub1 = root.find("lisi")
sub1.set("xuehao","20190101")

#修改sub2的数据值
sub2 = root.find("zhangsan")
sub2.text = "我是张三"

#写回原文件
updateTree.write("04.xml")