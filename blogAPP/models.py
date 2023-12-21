from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse_lazy('article-detail', args=(str(self.id)))
    
