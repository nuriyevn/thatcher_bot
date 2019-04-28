from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^thatcher$', views.thatcher, name='thatcher'),
    url(r'^zori$', views.zori, name='zori'),
    url(r'^calculate$', views.calculate, name='calculate'),
    url(r'^setting', views.setting, name='setting'),
    url(r'secure', views.secure, name='secure'),
    url(r'sign', views.sign, name='sign'),
]
