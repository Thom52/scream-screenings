from django.db import models
from datetime import timedelta
from cloudinary.models import CloudinaryField

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    screening_datetime = models.DateTimeField(null=True, blank=True)
    release_date = models.DateField()
    description = models.TextField()
    duration = models.DurationField(default=timedelta(minutes=90))
    director = models.CharField(max_length=255)
    poster = CloudinaryField('poster', default='https://res.cloudinary.com/dqn4oyjlv/image/upload/v1738684919/default-poster_hjhwj4.webp')

    def save(self, *args, **kwargs):
        # Automatically generate the slug from the title before saving
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title