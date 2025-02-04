from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'poster')
    search_fields = ('title',)

admin.site.register(Movie)