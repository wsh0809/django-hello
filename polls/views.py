from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world ! This is Polls index!")

def detail(request, question_id):
    return HttpResponse('Yot are looking at question %s.' % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)
