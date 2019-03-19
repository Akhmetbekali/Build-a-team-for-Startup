from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm, EditProfileForm


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


def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


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


def catalog(request):
    args = {'user': request.user}
    return render(request, 'accounts/users_catalog.html', args)
