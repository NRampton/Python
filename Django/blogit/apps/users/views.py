from django.shortcuts import HttpResponse, redirect

# Create your views here.


def index(request):
    return HttpResponse('placeholder to later display all the list of users')


def register(request):
    return HttpResponse('placeholder for users to create a new user record')


def new(request):
    return redirect('/users/register')


def login(request):
    return HttpResponse('placeholder for users to login')
