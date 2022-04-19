from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.template import loader
from .models import Article
# Create your views here.

class listView(generic.ListView):
    template_name = 'spider/list.html'
    context_object_name = 'last_article_list'

    def get_queryset(self):
        """Return the last article list"""
        return Article.objects.order_by('-create_time')[:5]

def index(request):
    template = loader.get_template('spider/index.html')
    context = {
        "url": "www.baidu.com",
    }
    return HttpResponse(template.render(context, request))

def test(request, a):
    b = 50
    return HttpResponse(a & b)
    # return render(request, 'spider/test.html', context={'res': a | b })