from django.conf.urls import include,url

from django.contrib import admin
from rescue.views import ProfileImageView
admin.autodiscover()

urlpatterns = [
    url(r'^profile_image_upload/', ProfileImageView.as_view(), name='profile_image_upload'),
    ]
