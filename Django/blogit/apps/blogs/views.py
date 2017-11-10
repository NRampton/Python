from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    print request
    response = "placeholder to later display the full list of blogs"
    return HttpResponse(response)


def new(request):
    response = "placeholder to display a form to create a new blog"
    return HttpResponse(response)


def create(request):
    return redirect('/blogs/')


def number(request, number):
    response = "placeholder to display blog {}".format(number)
    return HttpResponse(response)


def edit(request, number):
    response = "placeholder to edit blog {}".format(number)
    return HttpResponse(response)


def destroy(response, number):
    return redirect('/blogs/')
