from django.shortcuts import render, get_object_or_404
from .models import Film

# Create your views here.

def film_list(request):
    films = Film.objects.filter(is_coming_soon=False)
    hero_films = Film.objects.filter(is_hero_image=True)
    return render(request, 'films.html', {
        'films': films,
        'hero_films': hero_films,
        
        })

def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    return render(request, 'films_detail.html', {'film': film})


    