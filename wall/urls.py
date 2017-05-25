from django.conf.urls import url

from . import views

urlpatterns = [
    # ссылка на главную страницу.
    url(r'^$', views.general , name='general'),
    # ссылка на страницу моего класса
    url(r'^class/$', views.classes, name='class'),
    # ссылка на страницу для родителей
    url(r'^parents/$', views.parent, name='parent'),
    # ссылка на страницу для коллег
    url(r'^colleagues', views.colleagues, name='colleagues'),

    url(r'^partial/$', views.partial, name='partial'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/new_partial/$', views.postPartial_new, name='post_partial_new'),
]