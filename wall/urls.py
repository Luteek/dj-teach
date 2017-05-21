from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wall, name='wall'),
    url(r'^partial/$', views.partial, name='partial'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/new_partial/$', views.postPartial_new, name='post_partial_new'),
]