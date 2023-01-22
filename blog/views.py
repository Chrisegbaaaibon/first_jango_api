from django.shortcuts import render
from django.http import HttpResponse


posts = [
      {
            'author': 'Lana DelRay',
            'title': 'Blog Post',
            'content': 'lorem ispium dolor et blah blah blah',
            'date_posted': 'August 27, 2023'
      },
      {
            'author': 'Ghostcod3r',
            'title': 'Introduction to Django',
            'content': 'Django is a python framework for building web api and stuffs like that blah blah blah',
            'date_posted': 'August 31, 2023'
      },
      {
            'author': 'Ghostcod3r',
            'title': 'Introduction to Django',
            'content': 'Django is a python framework for building web api and stuffs like that blah blah blah',
            'date_posted': 'August 31, 2023'
      },
      {
            'author': 'Ghostcod3r',
            'title': 'Introduction to Django',
            'content': 'Django is a python framework for building web api and stuffs like that blah blah blah',
            'date_posted': 'August 31, 2023'
      },
      {
            'author': 'Ghostcod3r',
            'title': 'Introduction to Django',
            'content': 'Django is a python framework for building web api and stuffs like that blah blah blah',
            'date_posted': 'August 31, 2023'
      }
]

def Home(request):
      context={
            'posts': posts
      }
      return render(request, 'blog/home.html', context)


def About(request):
      return render(request, 'blog/about.html',  {'title': 'About Us'})