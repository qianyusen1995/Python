age=int(input("请输入您的年龄（1~100之间的整数）："))
if age >=1 and age <=100:
     print("您输入的是有效年龄！")
if age >=60 or age<=4:
     print ("您享受免票政策，可以免票入园游玩")
else:
    print("您不符合免票政策，需要购买门票才能入园游玩")
