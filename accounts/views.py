from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def login_redirect(request):
    return redirect('account/home.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)
