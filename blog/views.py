from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Tim',
        'title': 'dummy title',
        'content': 'First post content',
        'date_posted': 'Jan 11, 2023'
    },
    {
        'author': 'Anna',
        'title': 'dummy title2',
        'content': 'Second post content',
        'date_posted': 'Jan 12, 2023'
    }
]

def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})