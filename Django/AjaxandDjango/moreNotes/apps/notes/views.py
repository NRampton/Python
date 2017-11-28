from django.shortcuts import render, redirect
from .models import Note

# Create your views here.


def index(request):
    context = {
        'notes': Note.objects.all().order_by('-id')
    }
    return render(request, 'notes/index.html', context)


def edit(request):
    pass


def select(request):
    pass


def destroy(request):
    note_id = request.POST['note_id']
    Note.objects.get(id=note_id).delete()
    context = {
        'notes': Note.objects.all().order_by('-id')
    }
    return render(request, 'notes/replacement_index.html', context)


def create(request):
    Note.objects.create(title=request.POST['title'], content="What should go here?")
    context = {
        'notes': Note.objects.all().order_by('-id')
    }
    return render(request, 'notes/replacement_index.html', context)
