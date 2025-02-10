from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #built-in
# users, posts => datas for the databases

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() #unrestricted
    date_posted = models.DateTimeField(default=timezone.now) # not timezone.now() => L5 5:34 told
    author = models.ForeignKey(User, on_delete=models.CASCADE) # when user deleted, their posts also deleted, we can change this as per our requirements
    
    def __str__(self):
        return self.title





# -----------

# date_posted = models.DateTimeField(auto_now=True) # will change whenever the post is updated
# date_posted = models.DateTimeField(auto_now_add=True) #current date, time when the post was done
    