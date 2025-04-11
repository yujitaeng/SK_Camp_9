from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    # templates 하위 경로
    return render(request, 'second/index.html')