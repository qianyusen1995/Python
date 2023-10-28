from flask import request,Flask
app=Flask(__name__)
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']  		#获取到上传的文件
        #保存到C盘下，并命名为 uploaded_file.txt
        f.save('C:\\uploaded_file.txt') 	
        return 'you have successed in uploading！'

    return '''
        <form action="" method="post" enctype="multipart/form-data">
            <p><input type=file name=file>
            <p><input type=submit value=上传>
        </form>
            '''
app.run(port=10000,debug=True)