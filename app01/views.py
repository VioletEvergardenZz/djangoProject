from django.shortcuts import render,HttpResponse,redirect

from app01.models import UserInfo


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

def info_list(request):
    # 1.获取数据库中所有的用户信息
    data_list=UserInfo.objects.all()
    print(data_list)
    return render(request,"info_list.html",{"data_list":data_list})

def info_add(request):
    if request.method == "GET":
        return render(request,'info_add.html')
    # 获取用户提交的数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    # 添加到数据库
    UserInfo.objects.create(name=user,password=pwd,age=age)
    # 自动跳转
    return redirect("/info/list")

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")