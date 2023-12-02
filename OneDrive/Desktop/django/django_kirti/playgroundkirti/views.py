from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):
    x = 1
    y=2
    return render(request, "hello.html", {'data': [1,2,3]})
