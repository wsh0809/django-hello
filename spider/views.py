from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
# Create your views here.

class IndexView(generic.DetailView):
    template_name = 'spider/index.html'

def index(request):
    return HttpResponse('Hello Will')

def test(request):
    return HttpResponse('Hello test')