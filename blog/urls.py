from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    # path('', views.hello, name='hello'),
    path('', views.index, name='index'),
]