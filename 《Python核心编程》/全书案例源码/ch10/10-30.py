from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from tools.resis_handler import connect_obj

def login(request):
    resp = redirect('/list_display/')
    resp.set_cookie('K','a') #设置Cookie的值
    return resp
#将Cookie的值展现出来
def display(request):
    print(request.COOKIES['K'])
    return HttpResponse('OK')