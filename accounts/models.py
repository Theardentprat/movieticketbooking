from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
from django.utils.timezone import now


# Create your models here

class Cinema(models.Model):
    cinema=models.AutoField(primary_key=True)
    role=models.CharField(max_length=30,default='cinema_manager')
    cinema_name=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=15)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.cinema_name

class Movie(models.Model):
    movie=models.AutoField(primary_key=True)
    movie_name=models.CharField(max_length=50)
    movie_trailer=models.URLField(max_length=300)
    movie_rdate=models.DateField(auto_now=True)
    movie_des=models.TextField()
    movie_rating=models.DecimalField(max_digits=3, decimal_places=1)
    movie_poster=models.ImageField(upload_to='movies/poster', default="movies/poster/not.jpg")
    movie_genre=models.CharField(max_length=50,default="Action | Comedy | Romance")
    movie_duration=models.DurationField(default=timedelta(hours=2, minutes=45, seconds=0))

    def __str__(self):
        return self.movie_name

class Shows(models.Model):
    shows=models.AutoField(primary_key=True)
    cinema=models.ForeignKey('Cinema',on_delete=models.CASCADE, related_name='cinema_show')
    movie=models.ForeignKey('Movie',on_delete=models.CASCADE, related_name='movie_show')
    time=models.TimeField(auto_now=True)
    date=models.DateField(max_length=15, default=now)
    price=models.IntegerField()

    def __str__(self):
        return self.cinema.cinema_name +" | "+ self.movie.movie_name +" | "+ str(self.time)
    
    class Meta:
        verbose_name_plural = _("Shows")

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shows = models.ForeignKey(Shows, on_delete=models.CASCADE)
    useat = models.CharField(max_length=100)
    discount = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)
    
    @property
    def useat_as_list(self):
        return self.useat.split(',')
    def __str__(self):
        return self.user.username +" | "+ self.shows.movie.movie_name +" | "+ self.useat
    
    class Meta:
        verbose_name_plural = _("Bookings")

