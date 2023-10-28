#�����Ҫ��ģ��
from bs4 import BeautifulSoup
import requests


#�������
if __name__ == '__main__':
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml']
    for url in urls:
#���ý���������ĺ���
        get_temperature(url)


def get_temperature(url):
#����ͷ�����汾�������
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/
537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#�ύ����  
    response = requests.get(url, headers=headers).content
#ʹ��BeautifulSoup����Ӧ���н���
    soup = BeautifulSoup(response, "lxml")
    #������ҳ��<div>��ǩ
    conmid = soup.find('div', class_='conMidtab')
    conmid2 = conmid.findAll('div', class_='conMidtab2')


#����conmid2�е�conMidtab2
for info in conmid2:
#ʹ����Ƭȡ������<tr>��ǩ
    tr_list = info.find_all('tr')[2:]
#ʹ��enumerate()��������Ԫ�ص�λ�ü�����
    for index, tr in enumerate(tr_list):
        td_list = tr.find_all('td')
        if index == 0:
#��ȡÿ����ǩ��text��Ϣ����ʹ��replace()���������з�ɾ��
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


#����̨�������״��
print(city_name, weather, wind, max, min)
#�½�һ���ı��ĵ�����������浽���ı��ĵ���
mylog = open("outputlog.txt", "a", encoding='GBK')
print(city_name, weather, wind, max, min, file=mylog)
mylog.close()


#GUI��ƣ�tkinterģ�������ͬ�Ŀؼ�����Button��Label��Text��
from tkinter import *  
import urllib.request  	#�����������󣬻�ȡ����
import gzip  			#ѹ���ͽ�ѹ��ģ��
import json  			#������õ�����
from tkinter import messagebox  #������ʾ���
#��tkinterģ�齨��������
root = Tk()


def main():
    #���봰��
    root.title('����״����ѯ')  #���ڱ���
#���ñ�ǩ������λ��
    Label(root, text='�������ѯ����').grid(row=0, column=0)
#�����
enter = Entry(root)
#����λ��
    enter.grid(row=0, column=1, padx=20, pady=20) 
#��������
    enter.delete(0, END)  
#����Ĭ���ı�
    enter.insert(0, '����')  
running = 1


def get_weather_data():
#��ȡ����������
    city_name = enter.get()
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    #��ַ1ֻ��Ҫ�������������ַ2��Ҫ������д���
    #print(url1)
    weather_data = urllib.request.urlopen(url1).read()
    #��ȡ��ҳ����
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #��ѹ��ҳ����
    weather_dict = json.loads(weather_data)
    #��json����ת��Ϊdict����
    if weather_dict.get('desc') == 'invilad-citykey':
        print(messagebox.askokcancel("��ʾ", "������ĳ��������󣬻�����������δ��¼�����ڳ���"))
    else:
        #print(messagebox.askokcancel('xing','bingguo'))
        show_data(weather_dict, city_name)


#���ݵ���ʾ
def show_data(weather_dict, city_name):
#��ȡ���ݿ�
    forecast = weather_dict.get('data').get('forecast')
#������
    root1 = Tk()
#�޸Ĵ��ڴ�С
    root1.geometry('650x280')
#�����ڱ���
    root1.title(city_name + '����״��')

    #���������б�
    for i in range(5):  #��ÿ������ݷ����б���
        LANGS = [(forecast[i].get('date'), '����'),
                 (forecast[i].get('fengxiang'), '����'),
                 (str(forecast[i].get('fengji')), '�缶'),
                 (forecast[i].get('high'), '�����'),
                 (forecast[i].get('low'), '�����'),
                 (forecast[i].get('type'), '����')]
#���
        group = LabelFrame(root1, text='����״��', padx=0, pady=0)
#���ÿ��
        group.pack(padx=11, pady=0, side=LEFT)
#�����ݷ�������
        for lang, value in LANGS:  
            c = Label(group, text=value + ': ' + lang)
            c.pack(anchor=W)
    Label(root1, text='����Ϊ�ó���δ����������״����', fg='green').
place(x=40, y=20, height=40)
#�˳���ť������
    Button(root1, text='ȷ�ϲ��˳�', width=10, command=root1.quit).place(x=500, y=230, width=80, height=40)  
    root1.mainloop()

#���ð���
Button(root, text="ȷ��", width=10, command=get_weather_data) \
    .grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text='�˳�', width=10, command=root.quit) \
    .grid(row=3, column=1, sticky=E, padx=10, pady=5)
#һ����⵽�¼�����ˢ�°󶨵İ�ť���
if running == 1:
    root.mainloop()  


#ʹ��pymysqlģ���������ݿ�
conn = pymysql.connect(host='localhost', user='root', passwd='123456', 
db='weather', port=3306, charset='utf8')
#�α�
cursor = conn.cursor()


cursor.execute('insert into weather1(city,weather,wind,max,min) values(%s,%s,%s,%s,%s)',(city_name, weather, wind, max, min))

#�ύ
conn.commit()
