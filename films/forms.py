from django import forms 
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'poster', 'cast', 'genre', 'release_date',
                  'duration', 'is_popular', 'is_coming_soon', 'is_family', 'is_hero_image']
        
