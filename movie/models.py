from django.db import models
from datetime import timedelta
from cloudinary.models import CloudinaryField

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    duration = models.DurationField(default=timedelta(minutes=90))
    director = models.CharField(max_length=255)
    poster = CloudinaryField('poster', default='https://res.cloudinary.com/dqn4oyjlv/image/upload/v1738684919/default-poster_hjhwj4.webp')

    def __str__(self):
        return self.title