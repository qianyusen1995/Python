#views.py
from app.models import Author  #引入一个类 
def query(request):
    #result=Author.objects.all()
    #返回数据库查询结果（sql:select * from Author），list类型
    result=Author.objects.values_list() 
    return render(   #将返回的数据渲染到页面中
        request,
        'query.html',
        {
            'title':'Query', #将查询结果渲染到app/query.html中的变量result中
            'result':result,   
            'year':datetime.now().year,
         }       
        )