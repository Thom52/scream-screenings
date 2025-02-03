from django.shortcuts import render

# Create your views here.
def movie(request):
    return render(request, 'movie/movie-detail.html')