from django.shortcuts import render
from films.models import Film
# Create your views here.

def index(request):
    """ 
    Renders the home page with cateogorised films.
    """

    popular_films = Film.objects.filter(is_popular=True)
    coming_soon = Film.objects.filter(is_coming_soon =True)
    hero_films = Film.objects.filter(is_hero_image=True)

    context = {
        'popular_films': popular_films,
        'coming_soon': coming_soon,
        'hero_films': hero_films,
    }

    return render(request, 'home/index.html', context)



def film_family(request):
    """
    Renders the family films page with only family films.
    """

    family_film = Film.objects.filter(is_family=True, is_coming_soon=False)
    hero_films = Film.objects.filter(is_family=True, is_hero_image=True)

    context = {
        'family_film': family_film,
        'hero_films': hero_films,
    }

    return render(request, 'family.html', context)
    