from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    # path('', views.hello, name='hello'),
    path('', views.index, name='index'),
    path('list-<int:lid>.html', views.list, name='list'),
    path('show-<int:sid>.html', views.show, name='show'),
    path('tag/<str:tag>', views.tag, name='tag'),
    path('s', views.search, name='search'),
    path('about', views.about, name='about'),
]
