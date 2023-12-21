from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    imagepost = models.ImageField(upload_to ='uploads/')
    body = models.TextField()
    date = models.DateField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
