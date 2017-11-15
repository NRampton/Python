from django.shortcuts import render, redirect
from models import User
# Create your views here.


def index(request):
    queryset = User.objects.all()
    return render(request, 'users/index.html', {'queryset': queryset})


def new(request):
    return render(request, 'users/new.html')


def edit(request, id):

    context = {
        'id': id

    }
    return render(request, 'users/edit.html', context)


def show(request, id):
    id = int(id)
    query = User.objects.get(id=id)
    print query
    context = {
        'id': id,
        'first_name': query.first_name,
        'last_name': query.last_name,
        'email': query.email,
        'created_at': query.created_at
    }
    print context
    return render(request, 'users/show.html', context)


def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    id = User.objects.last().id
    return redirect('/users/{}'.format(id))


def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('users/')


def update(request):
    return redirect('users/<id>')
