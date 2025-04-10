from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print('index 함수 호출!')
    return HttpResponse('<h1>Hello World🚀</h1>')

def hello(request):
    return HttpResponse('<h3>Hello Everyone~!</h3>')

def lunch(request):
    return HttpResponse('<h3>Lunch Time🍔🍕🌭🍟</h3>')
