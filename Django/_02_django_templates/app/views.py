from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'app/index.html')

def basics(request):
    context = {
        "name": "다람쥐",
        "height": 190,
        "hobby": ["도토리 먹기", "밤 까먹기", "호두 부숴먹기"],
        "today": datetime.now(),
        "users": [
            {"id": 1, "name": "김도연", "study": True},
            {"id": 2, "name": "이윤재", "study": True},
            {"id": 3, "name": "임수연", "study": False}
        ],
        "users": [],
        "eng_name": "Squirrel",
        "price": 12345.54321
    }
    return render(request, 'app/01_basics.html', context)

def layout(request):
    return render(request, 'app/02_layout.html')

def staticfiles(request):
    return render(request, 'app/03_staticfiles.html')

def urls(request):
    return render(request, 'app/04_urls.html')

def product(request, id):
    print("@@@@@ path variable [id] @@@@@", id)
    return render(request, 'app/04_urls.html')

def search(request):
    print(request.GET)
    q = request.GET.get('q')
    lang = request.GET.get('lang')
    return render(request, 'app/04_urls.html', {"q": q, "lang": lang})