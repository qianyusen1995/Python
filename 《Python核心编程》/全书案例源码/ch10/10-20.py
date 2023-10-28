<html>
  <head>
    {% if title %} 	#判断title变量是否存在
    <title>{{title}}</title>
    {% else %} 		#如果不存在
    <title>Hi,</title>
    {% endif %}		#结束判断
  </head>
  <body>
      <h1>Hi, {{user.name}}!</h1>
  </body>
</html>