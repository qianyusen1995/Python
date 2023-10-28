from flask import Flask,url_for
app=Flask(__name__)
@app.route('/')
def index():
    pass
@app.route('/example')
def index2():
    pass
@app.route('/example/<username>')
def index3(username):
    return url_for(index)
with app.test_request_context():
    print(url_for('index'))
    print(url_for('index2'))
    print(url_for('index3',username='abc'))