from flask import request
app=Flask(__name__)
@app.route('/')
def index():
    username = request.cookies.get('username')
#设置Cookie
@app.route('/')
def index():
    resp = make_response("hello world")
    resp.set_cookie('username', 'the username')
    return resp
#删除Cookie
def index():
    resp = make_response("hello world")
    #实质上就是将过期时间设置为0
    resp.set_cookie('username', 'the username',expires=0) 
    return resp