from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
'''
def home(request):
    return HttpResponse("<h1>Hello World</h1>")
'''
#Render html file#
def home(request):
    return render(request,'home.html',{'name':'Ganesh'})    

def add(request):
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    
    res = float(val1) + float(val2)
    return render(request,"results.html",{"result":res})

