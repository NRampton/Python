from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'cart/index.html')


def process(request):
    print request.POST
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'number' not in request.session:
        request.session['number'] = 0
    product = request.POST['product']
    if product == 'shirt':
        price = 20
    elif product == 'mug':
        price = 15
    elif product == 'bike':
        price = 820
    elif product == 'hat':
        price = 30
    request.session['subtotal'] = price * int(request.POST['quantity'])
    request.session['total'] += int(request.session['subtotal'])
    request.session['number'] += int(request.POST['quantity'])
    request.session.modified = True
    return redirect('/cart/checkout')


def checkout(request):
    return render(request, 'cart/checkout.html')


def clear(request):
    request.session['total'] = 0
    request.session['number'] = 0
    return redirect('/')
