from django.db import models 
from django.contrib.auth.models import User 
from embed_video.fields import EmbedVideoField # Thư viện để chèn video

from itertools import zip_longest

def split_comma(x):
    if x:
        return x.split(',')
    else:
        return []

# Create your models here.
class Viewer(User):
    dob = models.DateField() # Date of birth: Dùng để lưu ngày sinh của người dùng 

# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=1000) # Movie name
    year = models.CharField(max_length=10) # Year
    genre = models.CharField(max_length= 255) # Genre
    plot = models.CharField(max_length=2000) # Overview
    lang = models.CharField(max_length=255, default='English') # Language
    poster = models.CharField('image',max_length=255, null=True, blank=True) # Poster
    rating = models.DecimalField(decimal_places = 1, null = True, blank = True, max_digits=6) # Rating
    trailor = EmbedVideoField(null = True) # Trailor
    runtime = models.CharField(max_length=100, null = True) # Runtime 
    budget = models.CharField(max_length=1000, null = True) # Budget
    revenue = models.CharField(max_length=1000, null = True) # Revenue
    director = models.CharField(max_length=2000, null = True) # Director
    director_img = models.CharField(max_length=2000, null = True) # Link director
    top_cast = models.CharField(max_length=1000, null = True) # Top cast
    top_cast_img = models.CharField(max_length=1000, null = True) # Link top cast

    def director_and_img(self):
        directors = split_comma(self.director)
        images = split_comma(self.director_img)
        return zip_longest(directors, images)
    
    def top_cast_and_img(self):
        casts = split_comma(self.top_cast)
        images = split_comma(self.top_cast_img)
        return zip_longest(casts, images)

        
# Movie model
class ViewerMovie(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete= models.CASCADE) # Viewer: Khóa ngoại
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE) # Movie: Khóa ngoại
    watched = models.IntegerField(null = True) # Watched: Số lần xem phim 
    favourite = models.IntegerField(null = True) # Favourite: Số lần yêu thích phim
    rating = models.IntegerField(null = True) # Rating: Đánh giá phim
    review = models.CharField(max_length=150, null = True) # Review: Nhận xét phim
    rtime = models.DateTimeField(null = True) # Rtime: Thời gian đánh giá phim
