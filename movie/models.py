from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    director = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)

    def __str__(self):
        return self.title