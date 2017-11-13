from django.shortcuts import render, redirect
import datetime
# Create your views here.


def index(request):
    # print "Here's the list coming in that the template is trying to render:"
    # print request.session['words']
    return render(request,'words/index.html')


def process(request):
    print 'Here is the request that came in:'
    print request.POST
    # print "Here's request.session['words'] just before we check to see if it exists:"
    # print request.session['words']
    now = datetime.datetime.now().isoformat()
    if 'words' not in request.session:
        request.session['words'] = []
    if 'big' in request.POST:
        font_size = 2
    else:
        font_size = 1
    new_word = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'big': font_size,
        'time': now
    }
    print "Here's the new dictionary we're trying to append to request.session['words']:"
    print new_word
    request.session['words'].append(new_word)
    print "Here's the new, updated list of dictionaries under request.session['words']:"
    print request.session['words']
    request.session.modified = True         # This ended up fixing a problem where the session['words'] list wasn't updating correctly.
    return redirect('/')


def clear(request):
    request.session['words'] = []
    print request.session['words']
    return redirect('/')


# I'm creating a dictionary based on the request.POST information, then appending it to the list
# request.session['words']. But
