from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
      return HttpResponse('<h1>Home Page </h1>')


def About(request):
      return HttpResponse('<h2>About me</h2>')