from django.shortcuts import render
from django.http import HttpResponse

#/products ->index
# Create your views here.
def index(request):
    return HttpResponse('Hello world')


def new(request):
    return HttpResponse('new product')