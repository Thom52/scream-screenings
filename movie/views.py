from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def movie_list(request):
    # Fetch the first six movies in the Movie model
    movies = Movie.objects.all()[:6]
    return render(request, 'movie-list.html', {'movies': movies})

def movie_detail(request):
    # Fetch the movie by its ID or return a 404 if not found
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie-detail.html', {'movie': movie})