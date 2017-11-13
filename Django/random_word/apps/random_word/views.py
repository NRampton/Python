from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    print request.session
    context = {
        'random_string': get_random_string(length=14),
        'count': request.session['count']
    }
    return render(request,'random_word/index.html', context)


def reset(request):
    request.session['count'] = 0
    return redirect('/random_word')
