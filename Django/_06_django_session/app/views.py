from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    # username = request.session['username']
    username = request.session.get('username')
    print(f'========== username: {username} ==========')

    if username:
        request.session.set_expiry(10) # 60s

    return render(request, 'index.html')

def set_session(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username

        request.session['point'] = 12345
        request.session['prob'] = 12.345
        request.session['expired'] = True
        request.session['nums'] = [1, 2, 3, 4, 5]
        request.session['data'] = {
            'message': '이것은 session🐿️🐿️🐿️',
            'today': datetime.now().strftime('%Y-%m-%d'),
        }
    
    return redirect('app:index')


def clear_session(request):
    try:
        del request.session['point']
    except KeyError:
        pass

    request.session.flush()
    return redirect('app:index')