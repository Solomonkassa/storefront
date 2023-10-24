from django.shortcuts import render
from django.http import HttpResponse


def SayHello(request):
    return render(request,'hello.html', {'name': 'Solomon'})


