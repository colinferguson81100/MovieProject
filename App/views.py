from django.shortcuts import render
from .models import Movie
from django.views import generic

# Create your views here.

class MovieList(generic.ListView):
    model = Movie
    template_name = 'main.html'
    context_object_name = 'movies'

class MovieDetail(generic.DetailView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movie'
