from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html')),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logout.html')),
    url(r'^registration/$', views.registration),
    url(r'^profile/$', views.profile),
    url(r'^profile/edit$', views.edit_profile),
    url(r'^catalog/$', views.catalog),
]
