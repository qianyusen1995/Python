try:
   file = open(r"a.txt")
   print("文件被正常读取")
finally:
    print("Error")
    file.close()