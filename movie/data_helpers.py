import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie.settings") # Tên app bạn tạo ( QUAN TRỌNG ).
django.setup()
from myapp.models import Movie # Import Model đã tạo 

class DataObject():

    def __init__(self):
        pass

    def create(self, title, year, genre, plot, poster, rating, trailor):
        # Ta sẽ insert data bằng phương thức create
        return Movie.objects.create(title=title, year=year, genre=genre, plot=plot, poster=poster, rating=rating, trailor=trailor)