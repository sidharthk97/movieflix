from django.db import models

# Create your models here.


class Siteadmin(models.Model):
    username = models.CharField(max_length=80, default="username")
    password = models.CharField(max_length=40, default="password")

    class Meta:
        db_table = 'siteadmin'

class Movie(models.Model):
    name = models.CharField(max_length=150, default="movie name")
    language = models.CharField(max_length=30, default="")
    category = models.CharField(max_length=30, default="")
    year = models.CharField(max_length=10, default="")
    pic = models.ImageField(upload_to = 'siteadmin/', default='static/images/movielogo.png')
    video = models.FileField(upload_to = 'siteadmin/', default='static/images/movielogo.png')

    class Meta:
        db_table = 'movie'