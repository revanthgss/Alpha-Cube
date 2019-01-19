from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ussd/$', views.index, name='index'),
    url(r'^sms/$',views.sms, name='sms')
]