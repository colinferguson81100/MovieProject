from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content_rating = models.CharField(max_length=10)
    year = models.PositiveIntegerField()
    theme = models.CharField(max_length=100)
    runtime = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title