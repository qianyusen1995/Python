file = open(r"test.txt","r")
while True:
    line = file.readlines()
    if not line:
        break
    print(line)

['Hello\n', 'World\n', 'Python']