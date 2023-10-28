from flask import Flask, session, redirect, url_for,  request
app = Flask(__name__)
@app.route('/')
def index():
    if 'username' in session:
        #获取Session中的username
        return 'Logged in as %s' % session['username']  
    return 'Hi,You are not logged in'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #将表单中传入的username作为Session中的username传入
        session['username'] = request.form.get('username') 
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route('/logout')
def logout():
    #在Session中删除username，实际上就是设置其为空
    session.pop('username', None)  
    return redirect(url_for('index')) 	#跳转回index页面

app.config['SECRET_KEY']='123456' 		#设置密钥
app.run(port=5001,debug=True)