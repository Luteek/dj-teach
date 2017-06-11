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
    # ссылки на создание постов для каждой страницы
    url(r'^new_general$', views.new_postGeneral, name='new_postGeneral'),
    url(r'^new_class$', views.new_postClasses, name='new_postClass'),
    url(r'^new_parents$', views.new_postParents, name='new_postParents'),
    url(r'^new_colleagues$', views.new_postColleagues, name='new_postColleagues'),

    url(r'^post/(?P<type>\d+)/(?P<ident>\d+)/$', views.postGeneral, name='post'),

    # try url for edit post 
    url(r'^post/edit/(?P<type>\d+)/(?P<ident>\d+)/$', views.postEdit, name='edit'),

    url(r'^partial/$', views.partial, name='partial'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/new_partial/$', views.postPartial_new, name='post_partial_new'),
]