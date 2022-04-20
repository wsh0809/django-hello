from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Category, Tag, Tui, Banner, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui_id=2)[:6]
    tags = Tag.objects.all()
    return locals()

def index(request):
    allarticle = Article.objects.all().order_by('-id')[0:10]
    banner = Banner.objects.filter(is_active=True)[:4]
    tui = Article.objects.filter(tui_id=1)[:3]
    hot = Article.objects.all().order_by('views')
    link = Link.objects.all()
    return render(request, 'blog/index.html', locals())

def list(request, lid):
    list = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try :
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', locals())

def show(request, sid):
    show = Article.objects.get(id=sid)
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category).first()
    next_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'blog/show.html', locals())

def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'blog/tag.html', locals())

def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try :
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'blog/search.html', locals())

def about(request):
    return render(request, 'blog/page.html', locals())
