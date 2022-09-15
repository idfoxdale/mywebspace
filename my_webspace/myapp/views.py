from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def index(ishant):
    return HttpResponse('<h1>Homepage</h1>')

def learn_django(ishant):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_py(ishant):
    return HttpResponse('<h1>Hello Python</h1>')