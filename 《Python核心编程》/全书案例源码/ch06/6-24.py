import os,shutil
old = r"c:\Users\NAKAS\Desktop\Text1\Text2\Text4\test4.txt"
new = r"c:\Users\NAKAS\Desktop\Text1\Text3\Text4\test4.txt"
os.renames(old,new)
print("重命名成功")