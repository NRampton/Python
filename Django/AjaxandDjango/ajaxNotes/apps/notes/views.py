from django.shortcuts import render, redirect, HttpResponse
from .models import Note
# Create your views here.


def index(request):
    context = {
        'notes': Note.objects.all().order_by('-id')
    }
    return render(request, 'notes/index.html', context)


def create(request):
    Note.objects.create(title=request.POST['title'], content="What goes in this note?")
    return redirect('/')


def select(request):
    if request.method == 'POST':
        print request.POST
        note = Note.objects.get(id=request.POST['id'])
        context = {'note': note}
        return render(request, 'notes/replacement_form.html', context)
    else:
        return HttpResponse("Ooops, wrong HTTP request method.")


def update(request):
    note = Note.objects.get(id=id)
    note['content'] = request.POST['content']
    return redirect('/')


def destroy(request):
    note_id = request.POST['note_id']
    Note.objects.get(id=note_id).delete()
    return redirect('/')