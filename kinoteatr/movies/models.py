from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    schedule = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title
