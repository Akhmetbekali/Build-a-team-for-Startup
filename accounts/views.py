from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import RegistrationForm, EditProfileForm, ProfileUpdateForm, ProjectCreateForm, EditProjectForm
from accounts.models import ProjectPage


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
def profile(request, id=None):
    if id is None:
        return HttpResponseRedirect('/account/profile/%d/' % request.user.id)
    user = get_object_or_404(User, id=id)
    args = {'id': user.id, 'user': request.user}
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
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('/account/profile')
        else:
            args = {
                'p_form': p_form,
                'u_form': u_form,
            }
            return render(request, 'accounts/profile_edit.html', args)
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        args = {
            'p_form': p_form,
            'u_form': u_form,
        }
        return render(request, 'accounts/profile_edit.html', args)


def catalog(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    users = User.objects.all()
    return render(request, 'accounts/users_catalog.html', {
        'users': users,
        'current_user': user
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
        form = ProjectCreateForm(request.POST, owner=request.user)
        if form.is_valid():
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
    if request.method == 'POST':
        project_form = EditProjectForm(request.POST,
                                       # request.FILES,
                                       instance=request.project
                                       )
        if project_form.is_valid():
            project_form.save()

            return redirect('projects/projects_all.html')
        else:
            args = {
                'p_form': project_form
            }
            return render(request, 'projects/project_edit.html', args)
    else:
        project_form = EditProjectForm(instance=request.project)
        args = {
            'project_form': project_form,
        }
        return render(request, 'projects/project_edit.html', args)


@login_required(login_url="/account/login")
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
