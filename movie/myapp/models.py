from django.db import models 
from django.contrib.auth.models import User 
from embed_video.fields import EmbedVideoField # Thư viện để chèn video

# Create your models here.
class Viewer(User):
    dob = models.DateField()

# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    year = models.CharField(max_length=100)
    genre = models.CharField(max_length= 100)
    plot = models.CharField(max_length=2000) # Overview
    lang = models.CharField(max_length=70, default='English')
    poster = models.CharField('image',max_length=255, null=True, blank=True)
    rating = models.DecimalField(decimal_places = 2, null = True, blank = True, max_digits=6)
    trailor = EmbedVideoField(null = True)
    runtime = models.IntegerField(null = True)
    budget = models.IntegerField(null = True)
    revenue = models.IntegerField(null = True)
    
# Movie model
class ViewerMovie(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete= models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)
    watched = models.IntegerField(null = True)
    favourite = models.IntegerField(null = True)
    rating = models.IntegerField(null = True)
    review = models.CharField(max_length=150, null = True)
    rtime = models.DateTimeField(null = True)
