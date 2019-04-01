from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from accounts import views
from accounts.models import UserProfile, ProjectPage


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()


class EditProfileForm(forms.ModelForm):

    email = forms.EmailField(required=True)
    password = None

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'image',
            'speciality',
            'description'
        )


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = ProjectPage
        fields = (
            'title',
            'type',
            'description',
        )

    def save(self, commit=True):
        project = super(ProjectCreateForm, self).save(commit=False)
        project.owner = self.owner
        project.title = self.cleaned_data['title']
        project.type = self.cleaned_data['type']
        project.description = self.cleaned_data['description']

        if commit:
            project.save()

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
