from distutils.text_file import TextFile
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.
class Article(models.Model):
  title= models.CharField(max_length=200)
  body = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
class Comment(models.Model):
  body = models.TextField()
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
  user = models.ForeignKey(User, on_delete=models.CASCADE)