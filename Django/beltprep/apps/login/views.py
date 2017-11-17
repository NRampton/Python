from django.shortcuts import render, redirect

# Create your views here.


def index(req):
    return render(req, 'login/index.html')


def login(req):
    
