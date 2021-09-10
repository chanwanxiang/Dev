from django.shortcuts import render

from .models import cal

# Create your views here.

def index(request):
    return render(request,'index.html')

def calPage(request):
    return render(request,'cal.html')

def calc(request):
    valA = request.POST['valueA']
    valB = request.POST['valueB']
    result = int(valA) + int(valB)

    # cal.objects.create(valueA=valueA,valueB=valueB,result=result)

    return render(request,'rlt.html',context={'data':{result}})