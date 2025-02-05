from django.db import models
from django.contrib.auth.models import User
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
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically generate the slug from the title before saving
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
