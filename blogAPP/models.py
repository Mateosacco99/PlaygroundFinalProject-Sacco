from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse_lazy('article-detail', args=(str(self.id)))
    
