from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^thatcher$', views.index, name='index'),
    url(r'^zori$', views.zori, name='zori'),
    url(r'^calculate$', views.calculate, name='calculate'),
    url(r'secure', views.secure, name='secure'),
    url(r'sign', views.sign, name='sign'),
]
