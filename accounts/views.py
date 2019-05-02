from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import RegistrationForm, EditProfileForm, ProfileUpdateForm, ProjectCreateForm, EditProjectForm, AddCommentForm
from accounts.models import ProjectPage, UserProfile


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


def profile(request, id=None):
    if id is None:
        return HttpResponseRedirect('/account/profile/%d/' % request.user.id)
    user = get_object_or_404(User, id=id)
    args = {'user': user, 'current_user': request.user}
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


def projects_catalog(request):
    projects = ProjectPage.objects.all()
    return render(request, 'projects/projects_all.html', {
        'projects': projects,
    })


def project_page(request, id):
    project = get_object_or_404(ProjectPage, id=id)
    args = {'project': project, 'current_user': request.user}
    return render(request, 'projects/project.html', args)


@login_required(login_url="/account/login")
def create_project(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, owner=request.user)
        if form.is_valid():
            form.save()
            return redirect('../projects_catalog')
        else:
            args = {'form': form}
            return render(request, 'projects/create.html', args)
    else:
        form = ProjectCreateForm()
        args = {'form': form}
        return render(request, 'projects/create.html', args)


@login_required(login_url="/account/login")
def edit_project(request, id):
    project = get_object_or_404(ProjectPage, id=id)
    if request.method == 'POST':
        project_form = EditProjectForm(request.POST,
                                       instance=project
                                       )
        if project_form.is_valid():
            project_form.save()
            return HttpResponseRedirect('/account/project/%s/' % id)
        else:
            args = {
                'form': project_form
            }
            return render(request, 'projects/edit.html', args)
    else:
        project_form = EditProjectForm(instance=project)
        args = {
            'form': project_form,
            'project': project,
        }
        return render(request, 'projects/edit.html', args)


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


@login_required(login_url="/account/login")
def delete_project(request, id):
    project = get_object_or_404(ProjectPage, id=id)
    project.delete()
    return HttpResponseRedirect('/account/projects_catalog/')


@login_required(login_url="/account/login")
def add_comment_to_user(request, id):
    profile = get_object_or_404(UserProfile, id=id)
    if request.method == 'POST':
        form = AddCommentForm(request.POST, author=request.user, user_profile=profile)
        if form.is_valid():
            form.save()
            # TODO: хз куда редиректить
            return redirect('')
        else:
            args = {'form': form}
            # TODO:
            return render(request, '', args)
    else:
        form = AddCommentForm()
        args = {'form': form}
        # TODO:
        return render(request, '', args)


@login_required(login_url="/account/login")
def add_comment_to_project(request, id):
    project = get_object_or_404(ProjectPage, id=id)
    if request.method == 'POST':
        form = AddCommentForm(request.POST, author=request.user, project=project)
        if form.is_valid():
            form.save()
            # TODO: хз куда редиректить
            return redirect('')
        else:
            args = {'form': form}
            # TODO:
            return render(request, '', args)
    else:
        form = AddCommentForm()
        args = {'form': form}
        # TODO:
        return render(request, '', args)


def search(request):
    # Search by type of the project
    # Instead of 'lab' we need to get users input
    type = ProjectPage.objects.filter(type__contains='lab')

    # Search by keyword in description
    # Instead of '12' we need to get users input
    description = ProjectPage.objects.filter(description__contains='12')
    return render(request, 'projects/test.html', {
        'type': type,
        'keyword': description
    })
