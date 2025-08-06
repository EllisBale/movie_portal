from django.shortcuts import render
from films.models import Film
# Create your views here.

def index(request):
    popular_films = Film.objects.filter(is_popular=True)
    return render(request, 'home/index.html', {'popular_films': popular_films})

