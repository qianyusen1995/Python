from gensim.models import Word2Vec  #词向量
from random import choice
from os.path import exists
import warnings	#文件的不打印警告
import sys
from PyQt5 import QtCore, QtGui, QtWidgets         
class CONF:
    path = '古诗词.txt'   	#生成古诗词的来源是古诗词.txt文本
window = 16       			#滑窗大小的限制 
min_count = 60     			#过滤低频字  
size = 125         			#词向量的维度 
topn = 14          			#古诗词的开放度
    model_path = 'word2vec'
class Model:
    def __init__(self, window, topn, model):
        self.window = window
        self.topn = topn
        self.model = model                   		#词向量模型
        self.chr_dict = model.wv.index2word     	#字典
def poem_generator(self, title, form):
    filter = lambda lst: [t[0] for t in lst if t[0] not in ['，', '。']]
    if len(title) < 3:
        if not title:
            title += choice(self.chr_dict)
        for _ in range(3 - len(title)):
            similar_chr = self.model.similar_by_word(title[-1], self.topn // 2)
            similar_chr = filter(similar_chr)
            char = choice([c for c in similar_chr if c not in title])
            title += char
 poem = list(title)
        for i in range(form[0]):
            for _ in range(form[1]):
                predict_chr = self.model.predict_output_word(
                    poem[-self.window:], max(self.topn, len(poem) + 1))
                predict_chr = filter(predict_chr)
                char = choice([c for c in predict_chr if c not in poem[len(title):]])
                poem.append(char)
            poem.append('，' if i % 2 == 0 else '。')
        length = form[0] * (form[1] + 1)
        return '《%s》' % ''.join(poem[:-length]) + '\n' + ''.join(poem
[-length:])
        return '《%s》' % ''.join(poem[:-length]) + '\n' + ''.join(poem
[-length:])
   def main(config=CONF):
    form = {'五言绝句': (4, 5), '七言绝句': (4, 7)}
    m = Model.initialize(config)
    while True:
        title = input('请输入标题：').strip()
        try:
            poem = m.poem_generator(title, form['五言绝句'])
            print('\033[031m%s\033[0m' % poem)     
            poem = m.poem_generator(title, form['七言绝句'])
            print('\033[033m%s\033[0m' % poem)      
            print()
        except:
          return