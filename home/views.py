from django.shortcuts import render
from .models import PopularFilm
# Create your views here.

def index(request):
    films = PopularFilm.objects.all()
    return render(request, 'home/index.html', {'films': films})

