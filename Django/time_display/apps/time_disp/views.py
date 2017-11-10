from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.


def index(request):
    context = {
        'time': strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
    }
    return render(request,'time_disp/index.html', context)
