from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Movie
from .forms import CommentForm

#Create your views here.
def movie_list(request):
    # Fetch the first six movies in the Movie model
    movies = Movie.objects.all().order_by('screening_datetime')[:6]
    return render(request, 'movie/movie-list.html', {'movies': movies})


def movie_detail(request, movie_slug):
    # Fetch the movie by its ID or return a 404 if not found
    movie = get_object_or_404(Movie, slug=movie_slug)
    comments = movie.comments.all().order_by("-created_on")
    comment_count = movie.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.movie = movie
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(request, 'movie/movie-detail.html', {
        'movie': movie, 
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        }
    )

