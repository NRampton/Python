from django.shortcuts import render, redirect
import datetime
# Create your views here.


def index(request):
    return render(request,'words/index.html')


def process(request):
    print request.POST
    now = datetime.datetime.now().isoformat()
    if 'words' not in request.session:
        request.session['words'] = []
    if 'big' in request.POST:
        font_size = 1.5
    else:
        font_size = 1
    request.session['words'].append({
        'word': request.POST['word'],
        'color': request.POST['color'],
        'big': font_size,
        'time': now
    })
    print request.session['words']
    return redirect('/')


def clear(request):
    request.session['words'] = []
    return redirect('/')


# we need to pass in a word, a color, a "yes" if they checked that box, and the time.
