<html>
  <head>
    <title>learnflask</title>
  </head>
  <body>
    <h1>Hi, {{user.name}}!</h1>
    {% for content in contents %}
    <p>{{content}}</b></p>
    {% endfor %}
  </body>
</html>