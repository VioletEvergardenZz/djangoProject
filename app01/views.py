from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

# 去app目录下得templates目录寻找user_list.html
def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")

    # 如果是POST请求,获取用户提交的数据
    print(request.POST)
    username=request.POST.get("user")
    passwd=request.POST.get("pwd")
    if username == 'root' and passwd == '123':
        #return HttpResponse("登陆成功")
        return redirect("https://www.baidu.com/")

    # return HttpResponse("登录失败")
    return render(request,"login.html",{"error_msg":"用户名或密码错误"})
