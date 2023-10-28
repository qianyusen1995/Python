from flask import Flask,request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def index():
    return redirect(url_for('index2'))
@app.route('/index2')
def index2():
    return 'index2'
def index3():
abort(404)
app.run(port=5001,debug=True)