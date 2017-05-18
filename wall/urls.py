from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wall, name='wall'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]