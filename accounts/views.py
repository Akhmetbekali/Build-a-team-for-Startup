from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm, EditProfileForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

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
        u_form = EditProfileForm(request.POST,
                                 instance=request.user
                                 )


        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile
                                   )


        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/account/profile')
        else:
            args = {
            'p_form': p_form,
            'u_form': u_form
            }
            return render(request, 'accounts/profile_edit.html', args)
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        args = {
            'p_form': p_form,
            'u_form': u_form
        }
        return render(request, 'accounts/profile_edit.html', args)


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


def catalog(request):
    # Edit HERE if authenticated
    users = User.objects.all()
    return render(request, 'accounts/users_catalog.html', {
                'users': users,
            })

def current_user(request):
    args = {'user': request.user}

    return render(request, 'accounts/profile.html', args)