from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length = 400)
    last_name = models.CharField(max_length = 400)
    age = models.IntegerField()
class Song(models.Model):
    title = models.CharField(max_length = 400)
    date_released = models.Datefield()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste,on_delete=models.CASCADE)
class Lyric(models.Model):
    content = models.TextField()
    song_id = models.IntegerField(max_length = 400)

     

