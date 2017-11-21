from django.shortcuts import render, redirect
from forms import RegistrationForm

# Create your views here.


def index(request):
    form = RegistrationForm()
    context = {
        'myregistrationform': form
    }
    return render(request, 'formtest/index.html', context)


def register(request):
    if request.method == "POST":
        bound_form = RegistrationForm(request.POST)
        print bound_form.is_valid()
        return redirect('/')
