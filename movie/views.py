from django.shortcuts import render, get_object_or_404
from .models import Movie


#Create your views here.
def movie_list(request):
    # Fetch the first six movies in the Movie model
    movies = Movie.objects.all().order_by('screening_datetime')[:6]
    return render(request, 'movie/movie-list.html', {'movies': movies})


def movie_detail(request, movie_slug):
    # Fetch the movie by its ID or return a 404 if not found
    movie = get_object_or_404(Movie, slug=movie_slug)
    return render(request, 'movie/movie-detail.html', {'movie': movie})

