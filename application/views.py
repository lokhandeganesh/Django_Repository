from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
'''
def home(request):
    return HttpResponse("<h1>Hello World</h1>")
'''
#Render html file#
def home(request):
    return render(request,'home.html',{'name':'Ganesh'})    

def add(request)    :
    val1 = request.GET('num1')
    val2 = request.GET('num1')
    
    res = val1 + val2
    return render(request,"result.html",{"result":res})

