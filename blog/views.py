from django.shortcuts import render


posts = [
    {
        'author': 'Ankit',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2023',
    },

    {
        'author': 'Ankit2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2023',
    }
] #list of dictionaries of posts


def home(request): # func home, takes in the argument, "request" # THIS IS THE "HOME" VIEW
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context) #this is how the html file is rendered ; andar blog/templates nahi aayega

def about(request):
    return render(request, 'blog/about.html', )

def contact(request):
    return HttpResponse('<h1>Blog Contact</h1>')