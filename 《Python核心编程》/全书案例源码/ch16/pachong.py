#导入必要的模块
from bs4 import BeautifulSoup
import requests


#程序入口
if __name__ == '__main__':
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml']
    for url in urls:
#调用接下来定义的函数
        get_temperature(url)


def get_temperature(url):
#请求头，各版本的浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/
537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#提交请求  
    response = requests.get(url, headers=headers).content
#使用BeautifulSoup对响应进行解析
    soup = BeautifulSoup(response, "lxml")
    #查找网页的<div>标签
    conmid = soup.find('div', class_='conMidtab')
    conmid2 = conmid.findAll('div', class_='conMidtab2')


#遍历conmid2中的conMidtab2
for info in conmid2:
#使用切片取第三个<tr>标签
    tr_list = info.find_all('tr')[2:]
#使用enumerate()函数返回元素的位置及内容
    for index, tr in enumerate(tr_list):
        td_list = tr.find_all('td')
        if index == 0:
#获取每个标签的text信息，并使用replace()函数将换行符删除
            province_name = td_list[0].text.replace('\n', '')              city_name = td_list[1].text.replace('\n', '')
            weather = td_list[5].text.replace('\n', '')
            wind = td_list[6].text.replace('\n', '')
            max = td_list[4].text.replace('\n', '')
            min = td_list[7].text.replace('\n', '')
            print(province_name)
        else:
            city_name = td_list[0].text.replace('\n', '')
            weather = td_list[4].text.replace('\n', '')
            wind = td_list[5].text.replace('\n', '')
            max = td_list[3].text.replace('\n', '')
            min = td_list[6].text.replace('\n', '')


#控制台输出天气状况
print(city_name, weather, wind, max, min)
#新建一个文本文档，将结果保存到该文本文档中
mylog = open("outputlog.txt", "a", encoding='GBK')
print(city_name, weather, wind, max, min, file=mylog)
mylog.close()


#GUI设计，tkinter模块包含不同的控件，如Button、Label、Text等
from tkinter import *  
import urllib.request  	#发送网络请求，获取数据
import gzip  			#压缩和解压缩模块
import json  			#解析获得的数据
from tkinter import messagebox  #导入提示框库
#用tkinter模块建立根窗口
root = Tk()


def main():
    #输入窗口
    root.title('天气状况查询')  #窗口标题
#设置标签并调整位置
    Label(root, text='请输入查询城市').grid(row=0, column=0)
#输入框
enter = Entry(root)
#调整位置
    enter.grid(row=0, column=1, padx=20, pady=20) 
#清空输入框
    enter.delete(0, END)  
#设置默认文本
    enter.insert(0, '北京')  
running = 1


def get_weather_data():
#获取输入框的内容
    city_name = enter.get()
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    #网址1只需要输入城市名，网址2需要输入城市代码
    #print(url1)
    weather_data = urllib.request.urlopen(url1).read()
    #读取网页数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #解压网页数据
    weather_dict = json.loads(weather_data)
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        print(messagebox.askokcancel("提示", "你输入的城市名有误，或者天气中心未收录你所在城市"))
    else:
        #print(messagebox.askokcancel('xing','bingguo'))
        show_data(weather_dict, city_name)


#数据的显示
def show_data(weather_dict, city_name):
#获取数据块
    forecast = weather_dict.get('data').get('forecast')
#副窗口
    root1 = Tk()
#修改窗口大小
    root1.geometry('650x280')
#副窗口标题
    root1.title(city_name + '天气状况')

    #设置日期列表
    for i in range(5):  #将每天的数据放入列表中
        LANGS = [(forecast[i].get('date'), '日期'),
                 (forecast[i].get('fengxiang'), '风向'),
                 (str(forecast[i].get('fengji')), '风级'),
                 (forecast[i].get('high'), '最高温'),
                 (forecast[i].get('low'), '最低温'),
                 (forecast[i].get('type'), '天气')]
#框架
        group = LabelFrame(root1, text='天气状况', padx=0, pady=0)
#放置框架
        group.pack(padx=11, pady=0, side=LEFT)
#将数据放入框架中
        for lang, value in LANGS:  
            c = Label(group, text=value + ': ' + lang)
            c.pack(anchor=W)
    Label(root1, text='以下为该城市未来五日天气状况：', fg='green').
place(x=40, y=20, height=40)
#退出按钮的设置
    Button(root1, text='确认并退出', width=10, command=root1.quit).place(x=500, y=230, width=80, height=40)  
    root1.mainloop()

#布置按键
Button(root, text="确认", width=10, command=get_weather_data) \
    .grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text='退出', width=10, command=root.quit) \
    .grid(row=3, column=1, sticky=E, padx=10, pady=5)
#一旦检测到事件，就刷新绑定的按钮组件
if running == 1:
    root.mainloop()  


#使用pymysql模块连接数据库
conn = pymysql.connect(host='localhost', user='root', passwd='123456', 
db='weather', port=3306, charset='utf8')
#游标
cursor = conn.cursor()


cursor.execute('insert into weather1(city,weather,wind,max,min) values(%s,%s,%s,%s,%s)',(city_name, weather, wind, max, min))

#提交
conn.commit()
