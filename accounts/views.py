from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def login_redirect(request):
    return redirect('account/')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../login')
        else:
            args = {'form': form}
            return render(request, 'accounts/registration.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/registration.html', args)

@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile2.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
        else:
            args = {'form': form}
            return render(request, 'accounts/profile_edit.html', args)
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/profile_edit.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

@login_required
def catalog(request):
    args = {'user': request.user}
    return render(request, 'accounts/users_catalog.html', args)
