from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def index(request):
    context = {
        'posts': Post.objects.all().order_by('-id')
    }
    return render(request, 'posts/index.html', context)


def posts(request):
    Post.objects.create(content=request.POST['content'])
    return redirect('/')


def destroy(request):
    id = request.POST['id']
    Post.objects.get(id=id).delete()
    return redirect('/')
