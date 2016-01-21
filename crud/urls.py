"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from crud.views import home,Registrar

admin.autodiscover()

urlpatterns = [
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name':'index.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^$', login_required(home), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^empleados/', include('apps.empleados.urls',namespace='empleados'),name='empleados'),
    url(r'^registrar/$', Registrar, name='registrar'),
    url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name':'password_reset_form.html','email_template_name': 'password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name':'password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        {'template_name':'password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name':'password_reset_complete.html'}, name='password_reset_complete'),
]