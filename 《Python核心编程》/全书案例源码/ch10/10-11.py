from flask import request 	#导入request库
request.args.get("key")   	#用于获取请求的URL中的参数key的值
request.form.get("key", type=str, default=None) #用于获取表单中传入的参数
request.values.get("key")  	#用于获取所有参数
request.respond 			#用于获取其请求方式