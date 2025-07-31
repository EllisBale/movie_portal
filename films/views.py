from django.shortcuts import render
from .models import Film

# Create your views here.

def films_list(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})