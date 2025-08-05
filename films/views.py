from django.shortcuts import render, get_object_or_404
from .models import Film

# Create your views here.

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})

