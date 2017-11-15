from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
# Create your views here.


def index(req):
    queryset = Course.objects.all()
    return render(req, "courses/index.html", {'queryset': queryset})


def create(req):
    result = Course.manager.create_new_course(req.POST)
    if result[0]:
        return redirect('/')
    for key, message in result[1].iteritems():
        messages.error(req, message)
    return redirect('/')


def remove(req, id):
    queryset = Course.objects.get(id=id)
    return render(req, 'courses/remove.html', {'user': queryset})


def destroy(req, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
