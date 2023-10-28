import xml.etree.ElementTree as ET
tree = ET.parse('student.xml')
root = tree.getroot()

#打印根节点的标签和属性,获取
for child in root:
    print(child.tag, child.attrib)
for student in root.findall('student'):
    id = student.find('id').text
    age = student.find('age').text
    xuehao = student.find('xuehao').text
print(id,age,xuehao)