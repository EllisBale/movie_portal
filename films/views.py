from django.shortcuts import render, get_object_or_404
from .models import Genre

# Create your views here.

def film_list(request):
    genres = Genre.objects.prefetch_related('film_set')
    return render(request, 'films.html', {'genres': genres})