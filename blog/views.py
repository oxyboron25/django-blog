from django.shortcuts import render
from .models import Post #. coz, smae dir

def home(request): # func home, takes in the argument, "request" # THIS IS THE "HOME" VIEW
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #this is how the html file is rendered ; andar blog/templates nahi aayega

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def contact(request):
    return render(request, 'blog/contact.html', )