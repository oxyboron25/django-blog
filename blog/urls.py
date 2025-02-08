from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), #nothing => home page, landing page
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),

]
# This file contains the URL configurations for the blog app.
#
# The variable urlpatterns is a "list" of path() instances.
#
# Each path() instance represents a URL pattern and maps it to a view function.
#
# The arguments to path are:
#   1. The URL pattern to match. The pattern is a string that contains a
#      forward slash (/) as a separator between URL components.
#   2. The view function to call when the pattern is matched. This function
#      must take a HttpRequest object as its first argument.
#   3. The name of the URL pattern. This name is used to reverse-engineer URLs
#      from the view function names.

# The first and only path in the urlpatterns list matches the URL pattern ''.
# This pattern matches the root of the blog app's namespace.
#
# When this pattern is matched, the view function views.home is called.
#
# The name of this URL pattern is 'blog-home'. This name can be used to reverse
# the URL pattern from the view function name.


