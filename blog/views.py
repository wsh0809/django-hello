from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
# Create your views here.

def hello(request):
    return HttpResponse('欢迎使用Django！')

def index2(request):
    sitename = 'Will'
    url = '127.0.0.1:8000'
    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据模型'
    ]
    dict = {
        'name': 'Will',
        'qq': '1829872',
        'wx': '我就是11',
        'Email': 'wwe@qq.sos'
    }
    context = {
        'sitename': sitename,
        'url': url,
        'list': list,
        'dict': dict
    }
    return render(request, 'blog/index2.html', context)

def index(request):
    allarticle = Article.objects.all()
    context = {
        'allarticle': allarticle
    }
    return render(request, 'blog/index.html', context)
