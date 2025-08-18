from django.shortcuts import render
from films.models import Film
# Create your views here.

def index(request):
    popular_films = Film.objects.filter(is_popular=True)
    coming_soon = Film.objects.filter(is_coming_soon =True)
    return render(request, 'home/index.html', {
        'popular_films': popular_films,
        'coming_soon': coming_soon
        
        })

