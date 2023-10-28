file = open(r"test.txt","r")
while True:
    line = file.readline()
    if not line:
        break
    print(line)