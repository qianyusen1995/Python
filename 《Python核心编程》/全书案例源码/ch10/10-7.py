from flask import Flask  	#引入Flask
app = Flask(__name__) 		#创建一个Flask实例
@app.route('/') 			#将网址映射到这个函数上
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
app.run() 					#入口，执行