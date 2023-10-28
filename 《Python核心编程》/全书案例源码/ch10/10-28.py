from django.http import HttpResponse
from django.shortcuts import render_to_response
#表单页面
def test_form(request):
    return render_to_response("test.html")
#接收及处理表单请求数据
def test(request):
    request.encoding='utf-8'
    if request.method=="GET":
        message = '你的方式为get '
    elif request.method=="POST":
        message = '你的方式为post '
    else:
        message="未识别！"
    return HttpResponse(message)