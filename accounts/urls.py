from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html')),
    url(r'^registration/$', LoginView.as_view(template_name='accounts/registration.html')),
    url(r'^profile/$', LoginView.as_view(template_name='accounts/profile.html')),
]
