from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView


urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html')),
    url(r'^profile/logout/$', LogoutView.as_view(template_name='accounts/logout.html')),
    url(r'^registration/$', views.registration),
    url(r'^profile/change_password$', views.change_password),

    url(r'^reset_password/$', PasswordResetView.as_view(template_name="registration/password_reset_form.html")),
    url(r'^reset_password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset_password/complete/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^profile/$', views.profile),
    url(r'^profile/edit$', views.edit_profile),
    url(r'^catalog/$', views.catalog),

    url(r'^projects/?$', views.projects),
    url(r'^projects/create$', views.create_project),
    url(r'^projects/edit$', views.edit_project),
]
