from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Movie, Comment
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Movie.objects.filter()
        movie = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('movie-detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Movie.objects.filter()
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('movie-detail', args=[slug]))