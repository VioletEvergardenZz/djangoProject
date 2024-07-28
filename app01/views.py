from django.shortcuts import render,HttpResponse

# Create your views here.
# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

# 去app目录下得templates目录寻找user_list.html
def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")