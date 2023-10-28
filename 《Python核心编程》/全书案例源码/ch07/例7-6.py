import re
pattern = re.compile('[a-zA-Z]')
result = pattern.findall('qwer1234asdf5678')
print (result)
