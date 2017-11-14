from django.shortcuts import render, redirect
from random import randint

# Create your views here.


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = ""
    print request.session['gold']
    return render(request, 'gold/index.html')


def process(request, location):
    print location
    if location == "farm":      # the farm
        earnings = randint(10,20)
        request.session['gold'] += earnings
        request.session['log'] = "You earned {} gold working on the farm<br>".format(earnings) + request.session['log']
    if location == "cave":      # the cave
        earnings = randint(5, 10)
        request.session['gold'] += earnings
        request.session['log'] = "You found {} gold exploring a cave<br>".format(earnings) + request.session['log']
    if location == "house":     # the house
        earnings = randint(2, 5)
        request.session['gold'] += earnings
        request.session['log'] = "You earned {} gold working from home<br>".format(earnings) + request.session['log']
    if location == "casino":        #the casino
        earnings = randint(-50, 50)
        request.session['gold'] += earnings
        if earnings < 0:
            request.session['log'] = "Drat, you lost {} gold at the casino. Maybe that will teach you.<br>".format(earnings) + request.session['log']
        else:
            request.session['log'] = "All right, you won {} gold at the casino. Now quite while you're ahead!<br>".format(earnings) + request.session['log']
    return redirect('/')
