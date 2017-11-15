from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
# Create your views here.


def index(req):
    return render(req, "login/index.html")


def login(req):
    result = User.manager.login(req.POST)
    if result[0]:
        return redirect('/success')
    for key, message in result[1].iteritems():
        messages.error(req, message)
    return redirect('/')


def register(req):
    result = User.manager.createUser(req.POST)
    if result[0]:
        return redirect('/success')
    for key, message in result[1].iteritems():
        messages.error(req, message)
    return redirect('/')


def success(req):
    return render(req, "login/success.html")
