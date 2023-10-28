from matplotlib.pylab import date2num
import matplotlib.pyplot as plt
import mpl_finance as mpf
import tushare as ts
import datetime

# 获取三峡水利数据
data = ts.get_k_data('600116','2018-01-01')

# 更改日期格式
def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time
    
# 转换为二维数组
mat_data = data.as_matrix()
mat_data[:,0] = date_to_num(mat_data[:,0])

# 绘图
fig, ax = plt.subplots(figsize=(15,5))
fig.subplots_adjust(bottom=0.5)
mpf.candlestick_ochl(ax, mat_data, width=0.6, colorup='g', colordown='r', alpha=1.0)

# 设置显示细节
plt.grid(True)
x.xaxis_date()
plt.xticks(rotation=30)
plt.title('sanxia 2018')
plt.xlabel('Date')
plt.ylabel('Price')

# 显示
plt.show()