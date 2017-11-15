from django.shortcuts import render, redirect
from models import User
# Create your views here.


def index(request):
    queryset = User.objects.all()
    return render(request, 'users/index.html', {'queryset': queryset})


def new(request):
    return render(request, 'users/new.html')


def edit(request, id):
    id = int(id)
    query = User.objects.get(id=id)
    # print query
    context = {
        'id': id,
        'first_name': query.first_name,
        'last_name': query.last_name,
        'email': query.email,
        'created_at': query.created_at
    }
    return render(request, 'users/edit.html', context)


def show(request, id):
    id = int(id)
    query = User.objects.get(id=id)
    # print query
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
    return redirect('/')


def update(request, id):
    id = int(id)
    queryset = User.objects.get(id=id)
    print queryset
    print request.POST
    queryset.first_name = request.POST['first_name']
    queryset.last_name = request.POST['last_name']
    queryset.email = request.POST['email']
    queryset.save()
    return redirect('/users/{}'.format(id))
