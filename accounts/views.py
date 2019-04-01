from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm, EditProfileForm, ProfileUpdateForm, ProjectCreateForm
from accounts.models import ProjectPage
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    args = {'user': request.user}
    return render(request, 'accounts/home.html', args)


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


@login_required(login_url="/account/login")
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


@login_required(login_url="/account/login")
def edit_profile(request):
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST,
                                 instance=request.user
                                 )
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile
                                   )
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if u_form.is_valid() and p_form.is_valid() and password_form.is_valid():
            u_form.save()
            p_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect('/account/profile')
        else:
            args = {
                'p_form': p_form,
                'u_form': u_form,
                'password_form': password_form,
            }
            return render(request, 'accounts/profile_edit.html', args)
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        args = {
            'p_form': p_form,
            'u_form': u_form,
            'password_form': password_form,
        }
        return render(request, 'accounts/profile_edit.html', args)


def catalog(request):
    # Edit HERE if authenticated
    users = User.objects.all()
    return render(request, 'accounts/users_catalog.html', {
        'users': users,
    })


@login_required(login_url="/account/login")
def current_user(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


def projects(request):
    projects = ProjectPage.objects.all()
    return render(request, 'projects/projects_all.html', {
        'projects': projects,
    })


@login_required(login_url="/account/login")
def create_project(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.owner = request.user
            print(request.user)
            print(form.owner)
            form.save()
            return redirect('../projects')
        else:
            args = {'form': form}
            return render(request, 'projects/create.html', args)
    else:
        form = ProjectCreateForm()
        args = {'form': form}
        return render(request, 'projects/create.html', args)


@login_required(login_url="/account/login")
def edit_project(request):
    pass
