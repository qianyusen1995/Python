import math                		#导入math模块
def circle_area(r):            	#计算圆面积的函数  
    result = math.pi*r*r      	#计算圆面积
    return result            		#返回圆的面积

r = 20                      		#设置圆的半径为20
print('半径为%s的圆的面积为:%.2f' %(r,circle_area(r)))    
#输出圆的半径和面积（保留两位小数）