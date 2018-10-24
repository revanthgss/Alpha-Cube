from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^map/$', views.index, name='index')
]