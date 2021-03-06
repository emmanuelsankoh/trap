from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    album_name=models.CharField(max_length=25)
    artist_name=models.CharField(max_length=30)
    album_genre=models.CharField(max_length=10)
    album_cover=models.FileField()


    def get_absolute_url(self):
        return reverse('Bomba:index')


class Song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name=models.CharField(max_length=25)
    song_audio=models.FileField()

    def get_absolute_url(self):
        return reverse('Bomba:index', args=[str(self.pk)])
