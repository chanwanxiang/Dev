from django.shortcuts import render

# Create your views here.

# 添加index函数,返回index.html页面

def index(request):
    return render(request,'index.html')