import os
src = r"c:\Users\NAKAS\Desktop\test.txt"
dst = r"c:\Users\NAKAS\Desktop\test1.txt"
os.rename(src,dst)
print("文件重命名成功")