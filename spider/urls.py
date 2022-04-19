from django.urls import path

from . import views

app_name = 'spider'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.listView.as_view(), name='list'),
    path('test/<int:a>', views.test, name='test'),
]