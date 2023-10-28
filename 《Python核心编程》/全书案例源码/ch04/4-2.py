import math						#导入math模块
r = 20                    			#半径为20
result = lambda r:math.pi*r*r  	#计算圆面积的lambda表达式
print('半径为%s的圆的面积为:%.2f'%(r,result(r)))
#输出圆的半径和面积（保留两位小数）