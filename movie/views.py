from django.shortcuts import render
from movie.models import Movies

# Create your views here.
def home(request):
    all_movies = {
        'the_movie' : sorted(Movies.objects.all(), key=lambda x: x.likes, reverse=True),
        'home' : 'active',
    }
    return render(request, 'movie/home.html', context=all_movies)

def addmovie(request):
    if request.method == "POST":
        person_name = request.POST['f_name']
        movie_name = request.POST['movie_name']
        movie_desc = request.POST['movie_desc']
        gen = ", ".join(request.POST.getlist('genres'))
        new_movie = Movies(title=movie_name, description=movie_desc, genres=gen)
        new_movie.save()
    return render(request, 'movie/addmovie.html', context={'addmovie': "active"})