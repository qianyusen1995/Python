def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username =='lisi' and pwd == '12345':
            request.session['IS_LOGIN'] = True       #设置Session
        return redirect('/home/')  
    return render(request,'login.html') 

def home(request):
    #获取Session里的值
    is_login = request.session.get('IS_LOGIN',False)   
    if is_login:
        return HttpResponse('order')
    else:
        return redirect('/login/')